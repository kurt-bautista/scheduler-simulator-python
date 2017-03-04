from collections import deque
from heapq import heappush, heappop

def fcfs(q):
    elapsed = 0
    while q:
        x = heappop(q)

        if elapsed <= x[0]:
            elapsed = x[0]

        print(elapsed, x[1] + 1, str(x[2].burst) + "X")
        elapsed += x[2].burst

def sjf(q):
    pass

def srtf(q):
    pass

def p(q):
    pass

def rr(q, t):
    elapsed = 0
    fifo = deque([])
    while q:
        temp = heappop(q)
        if elapsed >= temp[2].arrival:
            fifo.append(temp)
        else:
            heappush(q, temp)

        while fifo:
            # print(fifo)
            x = fifo.popleft()

            if elapsed <= x[0]:
                elapsed = x[0]
            
            endChar = "X\n"
            tempBurst = x[2].burst;
            if tempBurst > t:
                tempBurst = t
                endChar = "\n"
                x[2].burst -= t
                fifo.append(x)

            print(elapsed, x[1] + 1, tempBurst, end=endChar)
            elapsed += tempBurst

class Process:
    def __init__(self, arrival, burst, priority):
        self.arrival = arrival
        self.burst = burst
        self.priority = priority

testCases = int(input())

for i in range(testCases):
    ln = input()
    command = ln.split()
    processes = int(command[0])
    sched_type = command[1].lower()
    time_quantum = 0

    if sched_type == "rr":
        time_quantum = int(command[2])

    pQueue = []

    for j in range(processes):
        p = input()
        args = list(map(int, p.split()))

        if sched_type == "fcfs" or sched_type == "rr":
            heappush(pQueue, (args[0], j, Process(args[0], args[1], args[2])))
        elif sched_type == "sjf":
            heappush(pQueue, (args[1], args[0], j, Process(args[0], args[1], args[2])))
        elif sched_type == "srtf":
            heappush(pQueue, (args[0], j, Process(args[0], args[1], args[2])))
        elif sched_type == "p":
            heappush(pQueue, (args[2], j, Process(args[0], args[1], args[2])))
        else:
            print("Invalid scheduler")

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