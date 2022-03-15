import sys
import heapq
from collections import defaultdict
from turtle import distance

def cul_distance(a, b):
    return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5

n = int(sys.stdin.readline())
star_pos = []
for _ in range(n):
    star_pos.append(tuple(map(float, sys.stdin.readline().split())))
edges_dic = defaultdict(list)
for i in range(n - 1):
    for j in range(i + 1, n):
        distance = cul_distance(star_pos[i], star_pos[j])
        edges_dic[i].append((j, distance))
        edges_dic[j].append((i, distance))
q = [(0.0, 0, 0)]
visited = [False for _ in range(n)]
cnt = 0
ans = 0.0
while cnt < n:
    distance, a, b = heapq.heappop(q)
    if visited[a]:
        continue
    cnt += 1
    ans += distance
    visited[a] = True
    for node, distance in edges_dic[a]:
        if not visited[node]:
            heapq.heappush(q, (distance, node, a))
print(round(ans, 2))