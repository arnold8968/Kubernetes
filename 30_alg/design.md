### Design:
1.	Get current cpu usage in working pod level.(done)
2.	Build an assistant pod in each worker, they should implement algorithm 1 when there is a pod in pending. Thereafter, they should transfer a table to master and send a message to master whether their jobs are finished
3.	Build a scheduler in master. The scheduler should implement algorithm 2 and can handle beginning problem: when there is nothing information generating from current working jobs.

#### For task 2

There is the workflow:

1.  get pods name in the node writen by scheduler
2.  read pods current stage information from a csv file
3.  watch the kubernetes event
4.  when there is a pod in pending, run the algorithm and write the result in a json file to scheduler

#### For task 3
There is the workflow

1.  watch kubernetes
2.  when there is a pod in pending, read json reports from all worker nodes
3.  using data from worker nodes to scheduler the pod
4.  write the pod information into worker nodes json file

#### Additional design:

1.  When there are no jobs in any nodes, pick the one randomly
2.  When there are some jobs inside but nothing report received from worker node, pick the one with least job.
