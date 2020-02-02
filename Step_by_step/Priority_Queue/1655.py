import sys,heapq
max_heap = []
min_heap = []
N = int(sys.stdin.readline())
for i in range(N):
    data = int(sys.stdin.readline())
    if len(max_heap) == len(min_heap):
        heapq.heappush(max_heap,(-data,data))
    else:
        heapq.heappush(min_heap,data)
    if len(min_heap) != 0 and max_heap[0][1] > min_heap[0]:
        tmp1 = heapq.heappop(max_heap)[1]
        tmp2 = heapq.heappop(min_heap)
        heapq.heappush(min_heap,tmp1)
        heapq.heappush(max_heap, (-tmp2,tmp2))
    print(max_heap[0][1])


