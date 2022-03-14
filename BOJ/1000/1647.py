import sys
import heapq
from collections import defaultdict

n, m = map(int, sys.stdin.readline().split())
edges_dic = defaultdict(list)
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    edges_dic[a].append((b, c))
    edges_dic[b].append((a, c))
mst_nodes = [-1 for _ in range(n)]
visited = [True for _ in range(n)]
q = [(0, 1, 1)]
cnt = 0
ans = []
while cnt < n:
    cost, node, prev = heapq.heappop(q)
    if visited[node - 1] is False:
        continue
    cnt += 1
    ans.append(cost)
    visited[node - 1] = False
    mst_nodes[node - 1] = cost
    for dst, weight in edges_dic[node]:
        if visited[dst - 1] is True:
            heapq.heappush(q, (weight, dst, node))
print(sum(ans) - max(ans))