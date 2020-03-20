import sys
N,M,V = map(int,sys.stdin.readline().rstrip().split())
matrix = [[0]*(N+1) for _ in range(N+1)]
for i in range(M):
    link = list(map(int,sys.stdin.readline().split()))
    matrix[link[0]][link[1]] =1
    matrix[link[1]][link[0]] = 1

def dfs(cur,foot):
    foot += [cur]
    for search in range(len(matrix[cur])):
        if matrix[cur][search] == 1 and search not in foot:
            foot = dfs(search,foot)
    return foot

def bfs(start):
    queue = [start]
    foot=[start]
    while queue:
        cur = queue.pop(0)
        for search in range(len(matrix[cur])):
            if matrix[search][cur] and search not in foot:
                foot += [search]
                queue += [search]
    return foot
print(*dfs(V,[]))
print(*bfs(V))