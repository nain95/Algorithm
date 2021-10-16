import sys, heapq
from collections import defaultdict

def dijkstra(start, dis):
    heap = []
    res = dis[start]
    heapq.heappush(heap, [0, start])
    visited = [0] * (n + 1)
    for _ in range(n):
        cur_cost, cur = heapq.heappop(heap)
        visited[cur] = 1
        for i in range(1, n + 1):
            if visited[i] == 0: 
                heapq.heappush(heap, [dis[start][i], i])
                if cur_cost + dis[cur][i] < res[i]:
                    res[i] = cur_cost + dis[cur][i]

n, m, x = map(int, sys.stdin.readline().split())
distance = [[float('inf')] * (n + 1) for _ in range(n + 1)]
distance_rev = [[float('inf')] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    start, end, time = map(int, sys.stdin.readline().split())
    distance[start][end] = time
    distance_rev[end][start] = time
for i in range(1, n + 1):
    distance[i][i] = 0
    distance_rev[i][i] = 0
dijkstra(x, distance)
dijkstra(x, distance_rev)
ans = 0
for i in range(1, n + 1):
    if distance[x][i] + distance_rev[x][i] > ans:
        ans = distance[x][i] + distance_rev[x][i]
print(ans)
print(distance[x])
print(distance_rev[x])