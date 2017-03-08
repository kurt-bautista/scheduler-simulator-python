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
    elapsed = 0
    pq = []
    while q:
        counter = 0
        for item in q:
            if item.arrival <= elapsed:
                heappush(pq, [item.arrival, item.burst, item.index, item])
                q[counter] = None
                counter += 1
                
        q = [x for x in q if x is not None]

        while pq:
            x = heappop(pq)

            if elapsed < x[0]:
                elapsed = x[0]
            counter = 0
            for item in q:
                if item.arrival <= elapsed + x[1]:
                    heappush(pq, [item.arrival, item.burst, item.index, item])
                    q[counter] = None
                    counter += 1
            q = [a for a in q if a is not None]
            
            y = None if not pq else heappop(pq)
            if y:
                if y[1] < y[0] - elapsed:
                    x[0] = y[0]
                    x[1] = y[0] - elapsed
                    x[3].arrival = y[0]
                    x[3].burst = y[0] - elapsed
                    print(elapsed, x[2] + 1, x[1])
                    elapsed += x[1]
            else:
                print(elapsed, x[2] + 1, x[1])

def pRun(q):
    elapsed = 0
    # time = 0
    burst = 0
    #finalburst = 0
    q = sorted(q)
    working = []
    arrived = []
    notFirst = False
    grab = False
    skip = False
    while q:
        if notFirst is False:
            current = heappop(q)
            elapsed = current[0]
            
            grab = True
        
        
        if notFirst:
            if working:
                old = heappop(working)
            if arrived:
                if working:
                    heappush(arrived,[old[0], old[1], old[2], old[3]])
                old = heappop(arrived)
            if working is False and arrived is False:
                current = heappop(q)
                grab = True
                skip = True
                elapsed = current[0]


            if old[3].burst < q[0][3].arrival - elapsed and skip is False:
               #time += old[3].burst
               timestart = elapsed
               elapsed += old[3].burst
               heappush(arrived, old)
               print(timestart, old[3].index + 1, str(old[3].burst) + "X")
            elif old[3].burst == q[0][3].arrival - elapsed and skip is False:
                timestart = elapsed
                elapsed += old[3].burst
                print(timestart, old[3].index + 1, str(old[3].burst) + "X")
                current = heappop(q)
                grab = True
            elif old[3].burst > q[0][3].arrival - elapsed and skip is False:
                timestart = elapsed
                elapsed = q[0][3].arrival
                burst = q[0][3].arrival - elapsed
                current = heappop(q)
                grab = True
                old[3].burst -= burst
                heappush(arrived,[old[0],old[1],old[2],old[3]])
                
                print(timestart, old[3].index + 1, old[3].burst-(current[3].arrival-elapsed))
                
        if grab:
            heappush(working,[current[0], current[1], current[2], current[3]]) 
        notFirst = True
        grab = False
        skip = False

    while arrived:
        current = heappop(arrived)
        elapsed += current[3].burst
        print(elapsed, current[3].index +1, str(current[3].burst) + "X")

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

            print(elapsed, x[1] + 1, tempBurst, end=endChar)
            elapsed += tempBurst

class Process:
    def __init__(self, arrival, burst, priority, index):
        self.arrival = arrival
        self.burst = burst
        self.priority = priority
        self.index = index

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
            pQueue.append(Process(arrival, burst, priority, j))
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