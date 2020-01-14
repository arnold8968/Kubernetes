"""
This program will be implemented in a pod responsible for read data for all the pods in a given nodes
There is the workflow:
1.get pods name in the node from a json file writen by scheduler
2.read pods current stage information from a csv file
3.watch the kubernetes event
4.when there is a pod in pending, run the algorithm and write the result in a json file to scheduler
"""

import time
import random
import json
import pandas as pd


from kubernetes import client, config, watch

config.load_incluster_config()
v1 = client.CoreV1Api()

#since there are no method to get pod names belong to the pod,
#we have to read all pod names from a disk file

def get_pods(node_name):
    f = open("/data/"+node_name+".log","r")
    pods = f.read().split(",")
    pods = filter(lambda s:True if len(s)>0 else False,pods)
    return pods

#get information from given pod information disk file
def get_info(pod_name):
    info = pd.read_csv("/data/"+pod_name+".csv")



#run algorithm
def run_algorithm(node_name):
    pass


#when there is a pending job, do the calculation
def main():
    w = watch.Watch()
    for event in w.stream(v1.list_namespaced_pod, "default"):
        if event['object'].status.phase == "Pending":
            run_algorithm()