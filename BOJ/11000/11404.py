import sys
from math import inf


n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
cost = [[inf] * n for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    cost[a-1][b-1] = min(cost[a-1][b-1], c)

for k in range(n):
    cost[k][k] = 0
    for i in range(n):
        for j in range(n):
            cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])

for z in cost:
    for x in z:
        if x == inf:
            print(0, end=' ')
        else:
            print(x, end=' ')
    print()