import sys
from collections import deque


n, m = map(int, sys.stdin.readline().split())
matrix = []
answer = [[-1] * m for _ in range(n)]
start = [0, 0]
for i in range(n):
    matrix.append(list(map(int, sys.stdin.readline().split())))
    for j in range(m):
        if matrix[i][j] == 2:
            start = [i, j]
        if matrix[i][j] == 0:
            answer[i][j] = 0
visited = [[0] * m for _ in range(n)]
visited[start[0]][start[1]] = 1
queue = deque([start])
cnt = 0
hx, hy = [0, 0, 1, -1], [-1, 1, 0, 0]
while queue:
    count = len(queue)
    for _ in range(count):
        x, y = queue.popleft()
        answer[x][y] = cnt
        for k in range(4):
            nx, ny = x + hx[k], y + hy[k]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0 and matrix[nx][ny] == 1:
                queue.append([nx, ny])
                visited[nx][ny] = 1
    cnt += 1
for i in answer:
    for j in i:
        print(j, end=" ")
    print()
