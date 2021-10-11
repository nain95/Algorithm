import sys
from collections import deque, defaultdict

n, k = map(int, sys.stdin.readline().split())
queue = deque([n])
func = [[lambda x: x - 1, 1], [lambda x: x + 1, 1], [lambda x: x * 2, 0]]
distance = [float('INF')] * 200000
distance[n] = 0
while queue:
    cur = queue.popleft()
    if cur == k:
        break
    for f, weight in func:
        if 0 <= f(cur) < 200000 and distance[cur] + weight < distance[f(cur)]:
            if weight == 1:
                queue.append(f(cur))
            elif weight == 0:
                queue.appendleft(f(cur))
            distance[f(cur)] = distance[cur] + weight    
print(distance[k])
