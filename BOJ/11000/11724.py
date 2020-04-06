import sys
sys.setrecursionlimit(10000)

def dfs(v):
    visited[v] = True
    for e in data[v]:
        if not visited[e]:
            dfs(e)

n,m = map(int,sys.stdin.readline().split())
data = [[] for _ in range(n+1)]
visited = [False] * (n+1)
count = 0

for _ in range(m):
    u,v = map(int,sys.stdin.readline().split())
    data[u].append(v)
    data[v].append(u)

for j in range(1,n+1):
    if not visited[j]:
        dfs(j)
        count += 1
print(count)