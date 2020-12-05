import sys

def dfs(start):
    dx = [0,0,1,-1,1,-1,1,-1]
    dy = [1,-1,0,0,1,-1,-1,1]
    queue = [start]
    visited = [[0]*w for _ in range(h)]
    while queue:
        x, y = queue.pop()
        visited[x][y] = 1
        matrix[x][y] = 0
        for k in range(8):
            nx, ny = x+dx[k], y+dy[k]
            if 0 <= nx < h and 0 <= ny < w and visited[nx][ny] == 0:
                if matrix[nx][ny] == 1:
                    queue.append([nx, ny])


def land():
    for i in range(h):
        for j in range(w):
            if matrix[i][j] == 1:
                return [i,j]
    else:
        return []

while 1:
    w, h = map(int,sys.stdin.readline().split())
    if w == 0 and h == 0:
        break
    matrix = [[int(x) for x in sys.stdin.readline().split()] for _ in range(h)]
    cnt = 0
    ind = land()
    while ind:
        cnt += 1
        dfs(ind)
        ind = land()
    print(cnt)