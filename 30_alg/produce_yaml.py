import pandas as pd
import time

default_pool = "./pool/default_pool/"

scheduler = pd.read_csv("scheduler.csv")
for i in range(scheduler.shape[0]):
    yaml_file = scheduler.loc[i,"yaml"]
    job_name = scheduler.loc[i,"name"]
    names = job_name.split("-")
    name = names[1]+"-"+names[2]
    bench_mark = default_pool+name+".yaml"
    f = open(bench_mark,"r")
    info = f.read()
    f.close()
    info = info.replace("Needtoplaced",job_name)
    f = open(yaml_file,"w")
    f.write(info)
    f.close()
    time.sleep(1)
