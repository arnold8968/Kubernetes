import random
import os
import logging
import sys
import time
import numpy as np
import pandas as pd

logger = logging.getLogger(__name__)
logger.setLevel(level = logging.INFO)
handler = logging.FileHandler("log.txt")
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

def get_pool():
    f = open("pool/pool.txt","r")       # get the name for deeplearning methods, such as tf_birnn, tf_drnn 
    lines = f.read().split("\n")
    lines = filter(lambda s:len(s)>0,lines)
    f.close()
    return lines

def select_one(pool):
    return random.sample(pool,1)[0] # random chose one method

def create_yaml(name,job,scheduler):
    f_pool = open("pool/"+name+".yaml","r")# sample yaml method, replace the name and schedulerName
    conf = f_pool.read()
    conf = conf.replace("Needtoplaced",job+"-"+name)
    conf = conf.replace("scheduler-need-to-be-replaced",scheduler)
    f_pool.close()
    f_output = open(job+".yaml","w")
    f_output.write(conf)
    f_output.close()




#def add_scheduler(name,job,time): # name: tf_birnn, job: job1, time
#    second = random.randint(0,time)
#    with open("scheduler.csv","a") as f:
#        f.write(job+".yaml,"+str(second)+","+job+"-"+name+"\n")
#        logger.info("add "+job+"-"+name+",submitted on "+str(second))
#        f.close()


#def create_scheduler():
#    logger.info("create a new scheduler")
#    f = open("scheduler.csv","w")
#    f.write("yaml,seconds,name\n")
#    f.close()
#    
    
    
def main(job_num,time,scheduler):
    os.popen("rm *.yaml")
    logger.info("delete all previous yamls")
#    create_scheduler()
    pool = get_pool()
    job_list = []
    name_list = []
    for i in range(1,job_num+1):
        job = "job"+str(i)
        name = select_one(pool) # name: 
        create_yaml(name,job,scheduler)
        logger.info("create a "+name+" yaml named "+job+".yaml")
        job_list.append(job + ".yaml")
        name_list.append(job + "-" + name)
#        add_scheduler(name,job,time)
    logger.info("create a new scheduler")
    second = list(np.random.randint(time, size = job_num))
    second.sort()
    output = {'yaml':job_list,'seconds':second,'name':name_list}
    df = pd.DataFrame(output)
    df.to_csv('scheduler.csv')
    logger.info("successful created yamls and scheduler")


if __name__ == "__main__":
    job_num = int(sys.argv[1])
    time = int(sys.argv[2])
    scheduler = sys.argv[3]
    main(job_num,time,scheduler)

