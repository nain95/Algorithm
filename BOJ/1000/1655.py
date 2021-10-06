import sys, heapq
max_heap = []
min_heap = []
N = int(sys.stdin.readline())
for i in range(N):
    data = int(sys.stdin.readline())
    if len(max_heap) == len(min_heap):
        heapq.heappush(max_heap, -data)
    else:
        heapq.heappush(min_heap,data)
    if len(min_heap) != 0 and -max_heap[0] > min_heap[0]:
        max_value = -heapq.heappop(min_heap)
        min_value = heapq.heappop(max_heap)
        heapq.heappush(max_heap, max_value)
        heapq.heappush(min_heap, min_value)
    print(-max_heap[0])
