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
    while q or pq:
        process = None
        if pq:
            process = heappop(pq)
        else:
            process = heappop(q)

        counter = 0
        for p in q:
            if p[3].arrival <= elapsed + process[3].burst:
                heappush(pq, [p[3].burst, p[3].arrival, p[3].index, p[3]])
                q[counter] = None
                counter += 1
                
        q = [x for x in q if x is not None]

        if elapsed < process[3].arrival:
            elapsed = process[3].arrival

        print(elapsed, process[3].index + 1, str(process[3].burst) + "X")
        elapsed += process[3].burst

def srtf(q):
    elapsed = 0
    pq = []
    temp = None
    while q or pq:
        process = None
        # if temp:
        #     process = temp
        #     temp = None
        if pq:
            process = heappop(pq)
        else:
            process = heappop(q)

        counter = 0
        for p in q:
            if p[3].arrival < elapsed + process[3].burst:
                heappush(pq, p)
                q[counter] = None
                counter += 1
                
        q = [x for x in q if x is not None]

        if elapsed < process[3].arrival:
            elapsed = process[3].arrival

        sortedArrival = sorted(pq)
        found = False
        for nextProcess in sortedArrival:
            nextBurst = process[3].burst - abs(nextProcess[3].arrival - elapsed)
            if nextProcess[3].burst < nextBurst:
                process[0] = nextProcess[3].arrival
                process[1] -= nextProcess[3].arrival - elapsed
                process[3].arrival = nextProcess[3].arrival
                process[3].burst -= nextProcess[3].arrival - elapsed
                heappush(pq, process)
                if nextProcess[3].arrival - elapsed > 0:
                    print(elapsed, process[2] + 1, nextProcess[3].arrival - elapsed)
                    elapsed += nextProcess[3].arrival - elapsed
                found = True
                # temp = nextProcess
                # pq.remove(nextProcess)
                # heapify(pq)
                break
        if not found:
            print(elapsed, process[2] + 1, str(process[3].burst) + "X")
            elapsed += process[3].burst

def prio(q):
    elapsed = 0
    pq = []
    temp = None
    while q or pq:
        process = None
        if temp:
            process = temp
            temp = None
        elif pq:
            process = heappop(pq)
        else:
            process = heappop(q)

        counter = 0
        for p in q:
            if p[3].arrival < elapsed + process[3].burst:
                heappush(pq, p)
                q[counter] = None
                counter += 1
                
        q = [x for x in q if x is not None]

        if elapsed < process[3].arrival:
            elapsed = process[3].arrival

        sortedArrival = sorted(pq)
        found = False
        for nextProcess in sortedArrival:
            if nextProcess[3].priority < process[3].priority:
                process[0] = nextProcess[3].arrival
                process[1] -= nextProcess[3].arrival - elapsed
                process[3].arrival = nextProcess[3].arrival
                process[3].burst -= nextProcess[3].arrival - elapsed
                heappush(pq, process)
                if nextProcess[3].arrival - elapsed > 0:
                    print(elapsed, process[2] + 1, nextProcess[3].arrival - elapsed)
                    elapsed += nextProcess[3].arrival - elapsed
                found = True
                temp = nextProcess
                pq.remove(nextProcess)
                heapify(pq)
                break
        if not found:
            print(elapsed, process[2] + 1, str(process[3].burst) + "X")
            elapsed += process[3].burst

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
            heappush(q, temp)

        while fifo:
            x = fifo.popleft()

            if elapsed < x[0]:
                elapsed = x[0]
            
            endChar = "X\n"
            tempBurst = x[2].burst;

            temp = [item for item in q if item[2].arrival <= elapsed + tempBurst]
            heapify(temp)
            for item in temp:
                fifo.append(heappop(temp))
                heappop(q)

            if tempBurst > t:
                tempBurst = t
                endChar = "\n"
                x[2].burst -= t
                x[2].arrival = elapsed + tempBurst
                fifo.append(x)

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
            heappush(pQueue, (arrival, j, Process(arrival, burst, priority, j)))
        elif sched_type == "sjf" or sched_type == "srtf":
            heappush(pQueue, [arrival, burst, j, Process(arrival, burst, priority, j)])
        elif sched_type == "p":
            heappush(pQueue, [arrival, priority, j, Process(arrival, burst, priority, j)])
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
        prio(pQueue)
    elif sched_type == "rr":
        rr(pQueue, time_quantum)
    else:
        print("Invalid scheduler")