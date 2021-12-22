import sys
from collections import deque, defaultdict

n, k = map(int, sys.stdin.readline().split())
queue = deque([n])
func = [[lambda x: x - 1, 1], [lambda x: x + 1, 1], [lambda x: x * 2, 1]]
distance = [float("INF")] * 200000
distance[n] = 0
flag = True
cnt = [1] * 200000
while queue:
    length = len(queue)
    for _ in range(length):
        cur = queue.popleft()
        if cur == k:
            break
        for f, weight in func:
            if 0 <= f(cur) < 200000 and distance[cur] + weight < distance[f(cur)]:
                queue.append(f(cur))
                distance[f(cur)] = distance[cur] + weight
            elif 0 <= f(cur) < 200000 and distance[cur] + weight == distance[f(cur)]:
                queue.append(f(cur))
                distance[f(cur)] = distance[cur] + weight
                cnt[f(cur)] += 1
print(distance[k])
print(cnt[k])
