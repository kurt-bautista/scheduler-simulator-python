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
    while q:
        temp = heappop(q)
        if elapsed < temp[0]:
                elapsed = temp[0]
        fifo.append(temp)

        while fifo:
            x = fifo.popleft()

            if elapsed < x[0]:
                elapsed = x[0]
            
            endChar = "X\n"
            tempBurst = x[2].burst;

            temp = sorted([item for item in q if item[2].arrival <= elapsed + tempBurst])

            if x[2].timeRun == 0:
                x[2].firstRun = elapsed

            same = False
            if tempBurst > t:
                tempBurst = t
                endChar = "\n"
                x[2].burst -= t
                x[2].arrival = elapsed + tempBurst
                x[0] = elapsed + tempBurst
                x[2].timeRun += tempBurst
                for item in temp:
                    if item[2].arrival <= elapsed + tempBurst:
                        fifo.append(temp.pop(0))
                        heappop(q)
                if not fifo:
                    same = True
                fifo.append(x)
            else:
                if x[2].timeRun == 0:
                    x[2].timeRun = tempBurst
                else:
                    x[2].timeRun += tempBurst
                
            if not same:
                print(x[2].firstRun, x[1] + 1, x[2].timeRun, end=endChar)
                x[2].timeRun = 0

            elapsed += tempBurst

            

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
            heappush(pQueue, (args[2], j, Process(arrival, burst, priority, j)))
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