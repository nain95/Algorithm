import sys,heapq
from collections import defaultdict


def dijkstra(start):
    heap = []
    heapq.heappush(heap, (0, start))
    distance[start] = 0
    while heap:
        dist, now = heapq.heappop(heap)
        if distance[now] < dist:
            continue
        for data in graph[now]:
            cost = dist + data[1]
            if cost < distance[data[0]]:
                distance[data[0]] = cost
                heapq.heappush(heap, (cost, data[0]))


V,E = map(int,sys.stdin.readline().split())
K = int(sys.stdin.readline())
graph = defaultdict(list)
for _ in range(E):
    u, v, w = list(map(int, sys.stdin.readline().split()))
    graph[u].append([v, w])
distance = [float('inf')] * (V + 1)
dijkstra(K)
for i in range(1, len(distance)):
    if distance[i] == float('inf'):
        print('INF')
    else:
        print(distance[i])