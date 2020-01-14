"""
This program will be implemented as a scheduler in master node
There is the workflow
1.watch kubernetes
2.when there is a pod in pending, read json reports from all worker nodes
3.using data from worker nodes to scheduler the pod
4.write the pod information into worker nodes json file

Potential problems:
1.When there are no jobs in any nodes, pick the one randomly
2.When there are some jobs inside but nothing report received from worker node, pick the one with less jobs
3.The master node now has no permission for pvc. We need to debug it.
4.We need to test whether it has a influence to read json while writing something inside.
"""

import time
import random
import json

from kubernetes import client, config, watch

config.load_kube_config()
v1 = client.CoreV1Api()

scheduler_name = "foobar"


def nodes_available():
    ready_nodes = []
    for n in v1.list_node().items:
        for status in n.status.conditions:
            if status.status == "True" and status.type == "Ready":
                ready_nodes.append(n.metadata.name)
    return ready_nodes




def scheduler(name, node, namespace="default"):
    body = client.V1Binding()

    target = client.V1ObjectReference()
    target.kind = 'Node'
    target.apiVersion = 'v1'
    target.name = node

    meta = client.V1ObjectMeta()
    meta.name = name

    body.target = target
    body.metadata = meta

    try:
        # Method changed in clinet v6.0
        # return v1.create_namespaced_binding(body, namespace)
        # For v2.0
        res = v1.create_namespaced_binding_binding(name, namespace, body)
        if res:
            # print 'POD '+name+' scheduled and placed on '+node
            return True

    except Exception as a:
        print ("Exception when calling CoreV1Api->create_namespaced_binding: %s\n" % a)
        return False

def get_best_node():
    pass

def main():
    w = watch.Watch()
    for event in w.stream(v1.list_namespaced_pod, "default"):
        if event['object'].status.phase == "Pending" and event['object'].spec.scheduler_name == scheduler_name:
            try:
                res = scheduler(event['object'].metadata.name, random.choice(nodes_available()))
            except client.rest.ApiException as e:
                print json.loads(e.body)['message']


if __name__ == '__main__':
    main()