import sys
from collections import deque, defaultdict

n, k = map(int, sys.stdin.readline().split())
queue = deque([n])
func = [[lambda x: x - 1, 1], [lambda x: x + 1, 1], [lambda x: x * 2, 1]]
distance = [float("INF")] * 200000
distance[n] = 0
flag = True
depth = 0
backtracking = []
while queue:
    backtracking.append({})
    length = len(queue)
    for _ in range(length):
        cur = queue.popleft()
        if cur == k:
            break
        for f, weight in func:
            if 0 <= f(cur) < 200000 and distance[cur] + weight <= distance[f(cur)]:
                tmp = f(cur)
                queue.append(tmp)
                distance[tmp] = distance[cur] + weight
                backtracking[depth][tmp] = cur
    else:
        depth += 1
        continue
    break
    # depth += 1
            # elif 0 <= f(cur) < 200000 and distance[cur] + weight == distance[f(cur)]:
            #     tmp = f(cur)
            #     queue.append(tmp)
            #     distance[tmp] = distance[cur] + weight
print(distance[k])
# print(cur)
ans = [cur]
for i in range(depth-1, -1, -1):
    ans.append(backtracking[i][cur])
    cur = backtracking[i][cur]
for i in ans[::-1]:
    print(i,end=' ')