from collections import deque
from heapq import heappush, heappop, heapify

def fcfs(q):
    elapsed = 0
    while q:
        x = heappop(q)

        if elapsed < x[0]:
            elapsed = x[0]

        print(elapsed, x[1] + 1, str(x[2].burst) + "X")
        elapsed += x[2].burst

def sjf(q):
    elapsed = 0
    pq = []
    while q:
        counter = 0
        for p in q:
            if p.arrival <= elapsed:
                heappush(pq, (p.burst, p.index, p))
                q[counter] = None
                counter += 1
                
        q = [x for x in q if x is not None]

        while pq:
            x = heappop(pq)

            if elapsed < x[2].arrival:
                elapsed = x[2].arrival

            print(elapsed, x[2].index + 1, str(x[2].burst) + "X")
            elapsed += x[2].burst

def srtf(q):
    pass

def p(q):
    pass

def rr(q, t):
    elapsed = 0
    fifo = deque([])
    q = sorted(q)
    same = False
    while q or fifo:
        process = None
        if fifo and (True if not q else q[0][0] > elapsed and fifo[0][0] < q[0][0]) :
            process = fifo.popleft()
        else:
            process = q.pop(0)

        if elapsed < process[0]:
                elapsed = process[0]

        endChar = "X\n"
        burst = process[2].burst;
        
        if process[2].timeRun == 0:
            process[2].firstRun = elapsed

        if burst > t:
            burst = t
            endChar = "\n"
            process[2].burst -= t
            process[2].arrival = elapsed + burst
            process[0] = elapsed + burst
            process[2].timeRun += burst
            fifo.append(process)
            if len(fifo) == 1 and (True if not q else q[0][0] > elapsed + burst):
                same = True
            else:
                same = False
        else:
            same = False
            if process[2].timeRun == 0:
                process[2].timeRun = burst
            else:
                process[2].timeRun += burst

        if not same:
            print(process[2].firstRun, process[1] + 1, process[2].timeRun, end=endChar)
            process[2].timeRun = 0

        elapsed += burst 

class Process:
    def __init__(self, arrival, burst, priority, index):
        self.arrival = arrival
        self.burst = burst
        self.priority = priority
        self.index = index
        self.firstRun = arrival

    timeRun = 0
    firstRun = 0

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
        arrival = args[0]
        burst = args[1]
        priority = args[2]

        if sched_type == "fcfs" or sched_type == "rr":
            heappush(pQueue, [arrival, j, Process(arrival, burst, priority, j)])
        elif sched_type == "sjf":
            pQueue.append(Process(arrival, burst, priority, j))
        elif sched_type == "srtf":
            heappush(pQueue, (arrival, j, Process(arrival, burst, priority, j)))
        elif sched_type == "p":
            heappush(pQueue, (priority, j, Process(arrival, burst, priority, j)))
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