import sys
from collections import defaultdict
INF = float('inf')

def get_smallest_node(distance, visited):
    min_value = INF
    index = 0
    for i in range(1, n+1):
        if not visited[i] and distance[i] < min_value:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start, distance, visited):
    distance[start] = 0
    visited[start] = 1
    for i in dic[start]:
        distance[i] = dic[start][i]
    for _ in range(n - 1):
        now = get_smallest_node(distance, visited)
        visited[now] = 1
        for idx in dic[now].keys():
            cost = distance[now] + dic[now][idx]
            if cost < distance[idx]:
                distance[idx] = cost

n, e = map(int, sys.stdin.readline().split())
distance1 = [INF] * (n + 1)
distance2 = [INF] * (n + 1)
visited1 = [0] * (n + 1)
visited2 = [0] * (n + 1)
dic = defaultdict(dict)
for _ in range(e):
    a, b, c = map(int, sys.stdin.readline().split())
    #dic[a] = defaultdict(dict)
    #dic[b] = defaultdict(dict)
    dic[a][b] = c
    dic[b][a] = c
v1, v2 = map(int, sys.stdin.readline().split())
dijkstra(v1, distance1, visited1)
dijkstra(v2, distance2, visited2)
ans = min(distance1[1] + distance2[n], distance1[n] + distance2[1]) + distance1[v2]
if ans < float('inf'):
    print(ans)
else:
    print(-1)
