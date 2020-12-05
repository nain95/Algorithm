import sys,copy
from _collections import deque


def init():
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == '0':
                q.append([i, j, []])
                return


def bfs(cnt):
    answer = 0
    while q:
        length = len(q)
        print(q)
        for _ in range(length):
            x, y, k = q.popleft()
            if matrix[x][y] == '1':
                print(answer)
                return
            for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
                nx, ny, nk = x + dx, y + dy, copy.deepcopy(k)
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue
                c = matrix[nx][ny]
                if c.islower():
                    nk += c
                    nk = list(set(nk))
                elif c.isupper() and c.lower() in nk:
                    continue
                if not nk in matrix_check[nx][ny] and c != '#':
                    q.append((nx, ny, nk))
                    matrix_check[nx][ny] += [nk]
        answer += 1

    print(-1)


n,m = map(int,sys.stdin.readline().split())
matrix = []
matrix_check = [[[] for _ in range(m)] for _ in range(n)]
q = deque()
for i in range(n):
    matrix.append(list(sys.stdin.readline().rstrip()))
    for j in range(m):
        if matrix[i][j] == '0':
            cur = [i,j]
init()
bfs(0)