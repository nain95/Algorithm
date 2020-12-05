import sys,re
from _collections import deque

def init():
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == '0':
                q.append((i, j, 0))
                return


def bfs(cnt):
    while q:
        x, y, k = q.popleft()
        if matrix[x][y] == '1':
            print(matrix_check[x][y][k])
            return
        for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
            nx, ny, nk = x + dx, y + dy, k
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            c = matrix[nx][ny]
            if c.islower():
                nk |= (1 << (ord(c) - ord('a')))
            elif c.isupper() and not nk & (1 << (ord(c) - ord('A'))):
                continue
            if not matrix_check[nx][ny][nk] and c != '#':
                q.append((nx, ny, nk))
                matrix_check[nx][ny][nk] = matrix_check[x][y][k] + 1
    print(-1)


n,m = map(int,sys.stdin.readline().split())
matrix = []
matrix_check = [[[0]*64 for _ in range(m)] for _ in range(n)]
q = deque()
for i in range(n):
    matrix.append(list(sys.stdin.readline().rstrip()))
    for j in range(m):
        if matrix[i][j] == '0':
            cur = [i,j]
init()
bfs(0)