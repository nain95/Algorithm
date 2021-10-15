import sys
from collections import defaultdict, deque

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
bus = defaultdict(dict)
distance = [float('inf')] * (n + 1)
for _ in range(m):
    s, e, cost = map(int, sys.stdin.readline().split())
    if e in bus[s]:
        bus[s][e] = min(bus[s][e], cost)
    else:
        bus[s][e] = cost
start, end = map(int, sys.stdin.readline().split())
stack = deque([start])
distance[start] = 0
while stack:
    cur = stack.popleft()
    for e, cost in sorted(bus[cur].items(), key = (lambda x: x[1])):
        if distance[e] > distance[cur] + bus[cur][e]:
            distance[e] = distance[cur] + bus[cur][e]
            stack.append(e)
        else:
            pass
print(distance[end])