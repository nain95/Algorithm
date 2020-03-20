import sys,heapq
heap = []
N = int(sys.stdin.readline())
for _ in range(N):
    tmp = int(sys.stdin.readline())
    if tmp == 0:
        if heap == []:
            print(0)
        else:
            print(heapq.heappop(heap)[1])
    else:
        heapq.heappush(heap,(-tmp,tmp))