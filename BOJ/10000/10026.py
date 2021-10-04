import sys
from collections import deque

def bfs(x, y, color, visited):
    queue = deque([[x, y]])
    dx,dy = [1, -1, 0, 0], [0, 0, 1, -1]
    visited[x][y] = 1
    while queue:
        cur_x, cur_y = queue.popleft()
        for k in range(4):
            nx, ny = cur_x + dx[k], cur_y + dy[k]
            if nx < 0 or ny < 0 or nx >= n or ny >= n or visited[nx][ny] == 1 or matrix[nx][ny] not in color:
                continue
            else:
                queue.append([nx, ny])
                visited[nx][ny] = 1


n = int(sys.stdin.readline())
cnt = 0
cnt_blindness = 0
matrix = []
visited_normal = [[-1] * n for _ in range(n)]
visited_blindness = [[-1] * n for _ in range(n)]
for _ in range(n):
    matrix.append(list(sys.stdin.readline()))
for i in range(n):
    for j in range(n):
        if visited_normal[i][j] == -1:
            bfs(i, j, [matrix[i][j]], visited_normal)
            cnt += 1
        if visited_blindness[i][j] == -1:
            if matrix[i][j] == 'R' or matrix[i][j] == 'G':
                color_list = ['R', 'G']
            else:
                color_list = ['B']
            bfs(i, j, color_list, visited_blindness)
            cnt_blindness += 1
print(cnt, cnt_blindness)