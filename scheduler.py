from collections import deque
from heapq import heappush, heappop

def fcfs(q):
    pass

def sjf(q):
    pass

def srtf(q):
    pass

def p(q):
    pass

def rr(q, t):
    pass

class Process:
    def __init__(self, arrival, burst, priority, index):
        self.arrival = arrival
        self.burst = burst
        self.priority = priority
        self.index = index

testCases = raw_input()

for i in range(testCases):
    ln = raw_input()
    command = ln.split()
    processes = command[0]
    sched_type = command[1].lower()
    time_quantum = 0

    if sched_type == "rr":
        time_quantum = command[2]

    pQueue = []

    for j in range(processes):
        p = raw_input()
        args = p.split()

    if sched_type == "fcfs" or sched_type == "rr":
        heappush(pQueue, (args[0], j, Process(args[0], args[1], args[2], j + 1)))
    elif sched_type == "sjf":
        heappush(pQueue, (args[1], args[0], j, Process(args[0], args[1], args[2], j + 1)))
    elif sched_type == "srtf":
        heappush(pQueue, (args[0], j, Process(args[0], args[1], args[2], j + 1)))
    elif sched_type == "p":
        heappush(pQueue, (args[2], j, Process(args[0], args[1], args[2], j + 1)))
    else:
        print("Invalid scheduler")
        return

    print(i + 1) # Test case number

    if sched_type == "fcfs":
        fcfs(pQueue)
    elif sched_type == "sjf":
        sjf(pQueue)
    elif sched_type == "srtf":
        srtf(pQueue)
    elif sched_type == "p":
        p(pQueue)
    elif sched_type == "rr":
        rr(pQueue, time_quantum)
    else:
        print("Invalid scheduler")
        return