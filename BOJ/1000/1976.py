import sys


def find(x):
    while x != node[x]:
        x = node[x]
        node[x] = node[node[x]]
    return x

def union(x, y):
    x = find(x)
    y = find(y)
    if x <= y:
        node[y] = x
    else:
        node[x] = y


n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
node = [i for i in range(n)]
for i in range(n):
    for j, cmd in enumerate(list(map(int, sys.stdin.readline().split()))):
        if cmd == 1:
            union(i, j)
travel = list(map(int, sys.stdin.readline().split()))
answer = 'NO'
start = find(travel[0]-1)
for t in range(1, len(travel)):
    if start != find(travel[t]-1):
        break
else:
    answer = 'YES'
print(answer)