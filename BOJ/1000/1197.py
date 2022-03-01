import sys

def find(parent, x):
    if parent[x] != x:
        return find(parent, parent[x])
    return x

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

v, e = map(int, sys.stdin.readline().split())
line_list = [tuple(map(int, sys.stdin.readline().split())) for _ in range(e)]
parent = [i for i in range(v + 1)]
line_list = sorted(line_list, key = lambda x: x[2])
ans = 0
for a, b, c in line_list:
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        ans += c
print(ans)
