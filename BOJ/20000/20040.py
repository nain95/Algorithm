import sys

def find(a):
    if parent[a] == a:
        return a
    p = find(parent[a])
    parent[a] = p
    return p

def union(a, b):
    x, y = find(a), find(b)
    if x == y:
        return True
    elif x < y:
        parent[y] = x
    else:
        parent[x] = y
    return False


n, m = map(int, sys.stdin.readline().split())
parent = [i for i in range(n)]
ans = 0
flag = 0
for tmp in range(m):
    print(parent)
    a, b = map(int, sys.stdin.readline().split())
    if not flag and union(a, b):
        ans = tmp + 1
        flag = 1
print(ans)