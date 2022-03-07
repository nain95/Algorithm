import sys
import heapq

n ,k = map(int, sys.stdin.readline().split())
jewelry = sorted([tuple(map(int, sys.stdin.readline().split())) for _ in range(n)])
bag = sorted([int(sys.stdin.readline()) for _ in range(k)])
max_heap = []
result = 0
for weight in bag:
    while jewelry and weight >= jewelry[0][0]:
        heapq.heappush(max_heap, -jewelry[0][1])  # Max heap
        heapq.heappop(jewelry)
    if max_heap:
        result += heapq.heappop(max_heap)
    elif not jewelry:
        break
print(-result)