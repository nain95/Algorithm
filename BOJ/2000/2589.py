import sys
from collections import deque


def bfs(start):
    global h, w
    queue = deque([start])
    cnt = 0
    visited = [[0] * w for _ in range(h)]
    visited[start[0]][start[1]] = 1
    while queue:
        cnt += 1
        len_queue = len(queue)
        for _ in range(len_queue):
            x, y = queue.popleft()
            dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
            for k in range(4):
                nx, ny = x + dx[k], y + dy[k]
                if 0 <= nx < h and 0 <= ny < w and visited[nx][ny] == 0 and matrix[nx][ny] == 'L':
                    queue.append([nx,ny])
                    visited[nx][ny] = 1
    return cnt-1


if __name__ == "__main__":
    h,w = map(int,sys.stdin.readline().split())
    answer = 0
    matrix = []
    L_list = []
    for i in range(h):
        matrix.append(list(sys.stdin.readline().rstrip()))
        for j in range(w):
            if matrix[i][j] == 'L':
                L_list.append((i,j))
    for x, y in L_list:
        if 0 <= x-1 and x+1 < h and matrix[x-1][y] == 'L' and matrix[x+1][y] == 'L':
            continue
        elif 0 <= y-1 and y+1 < w and matrix[x][y-1] == 'L' and matrix[x][y+1] == 'L':
            continue
        else:
            answer = max(answer, bfs((x, y)))
    print(answer)