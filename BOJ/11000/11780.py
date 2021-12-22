import sys
from math import inf
from collections import deque


def devide(x, y):
    k = k_list[x][y]
    if k_list[x][k] != -1:
        answer.append(k_list[x][k])
        devide(x, k)
    #if k_list[x][y] != -1:
    #    answer.append(k_list[x][y])
    if k_list[k][y] != -1:
        answer.append(k_list[k][y])
        devide(k, y)


n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
cost = [[inf] * n for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    cost[a-1][b-1] = min(cost[a-1][b-1], c)
k_list = [[-1] * n for _ in range(n)]
for k in range(n):
    cost[k][k] = 0
    for i in range(n):
        for j in range(n):
            if cost[i][j] > cost[i][k] + cost[k][j]:
                k_list[i][j] = k
            cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])
for z in cost:
    for x in z:
        if x == inf:
            print(0, end=' ')
        else:
            print(x, end=' ')
    print()

for x in range(n):
    for y in range(n):
        if x == y or cost[x][y] == inf:
            print(0)
        elif k_list[x][y] != -1:
            answer = deque([])
            k = k_list[x][y]
            devide(x, k)
            #answer.append(k)
            #devide(k, y)
            answer.appendleft(x)
            answer.append(y)
            print(f"{len(answer)}", end=" ")
            for a in answer:
                print(a + 1, end=" ")
            print()
        else:
            print("2", end=' ')
            print(x + 1, y + 1)