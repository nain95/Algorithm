import sys
from collections import deque

def burn():
    tmp = fire[:]
    res = []
    for x, y in tmp:
        for k in range(4):
            nx, ny = x + dx[k] , y + dy[k]
            if 0 <= nx < r and 0 <= ny < c and (matrix[nx][ny] == '.'or matrix[nx][ny] == 'J'):
                matrix[nx][ny] = 'F'
                res.append((nx,ny))
    return res
    

def check_escape(x, y):
    if x == 0 or x == r-1:
        return 1
    elif y == 0 or y == c-1:
        return 1
    return 0

r, c = map(int ,sys.stdin.readline().split())
dx, dy = (0,0,1,-1),(1,-1,0,0)
matrix = []
fire = []
for i in range(r):
    matrix.append(list(sys.stdin.readline().rstrip()))
    for j in range(c):
        if matrix[i][j] == 'J':
            player = (i, j)
        elif matrix[i][j] == 'F':
            fire.append((i, j))
queue = deque([player])
visited = [[-1] * c for _ in range(r)]
visited[player[0]][player[1]] = 1
time = 0
while queue:
    fire = burn()
    time += 1
    length = len(queue)
    for _ in range(length):
        x, y = queue.popleft()
        if check_escape(x, y):
            print(time)
            exit()
        for k in range(4):
            nx, ny = x + dx[k] , y + dy[k]
            if 0 <= nx < r and 0 <= ny < c and matrix[nx][ny] == '.' and visited[nx][ny] == -1:
                visited[nx][ny] = 1
                queue.append((nx, ny))
print('IMPOSSIBLE')