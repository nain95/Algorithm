import sys

def find(a):
    while a != node[a]:
        a = node[a]
        node[a] = node[node[a]]
    return a

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        node[a] = b
    else:
        node[b] = a

def dfs(x, y):
    while 1:
        dx, dy = direct[matrix[x][y]]
        nx, ny = x + dx, y + dy
        matrix[x][y] = 'F'
        if matrix[nx][ny] == 'F':
            if find(nx * m + ny) != find(x * m + y):
                return 0
            else:
                return 1
        else:
            union(nx * m + ny, x * m + y)
            x, y = nx, ny

n, m = map(int, sys.stdin.readline().split())
matrix = []
node = [i for i in range(n * m)]
direct = {'D' : (1, 0), 'U' : (-1, 0), 'L' : (0, -1), 'R' : (0, 1)}
for _ in range(n):
    matrix.append(list(sys.stdin.readline().rstrip()))
ans = 0
for i in range(n):
    for j in range(m):
        if matrix[i][j] != 'F':
            ans += dfs(i, j)
print(ans)
