import sys
from collections import deque

def bfs(c, w, h):
    start, end = c
    res = float('inf')
    dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
    q = deque([start + [-1, 0]])
    visited = [[float('inf')] * w for _ in range(h)]
    visited[start[0]][start[1]] = 0
    while q:
        x, y, direction, cnt = q.popleft()
        if cnt != visited[x][y]:
            continue
        if [x,y] == end:
            res = cnt
        for k in range(4):
            tmp_cnt = cnt
            nx, ny = dx[k] + x, dy[k] + y
            if 0 <= nx < h and 0 <= ny < w and matrix[nx][ny] != '*':
                if direction != -1 and direction != k:
                    tmp_cnt += 1
                    if tmp_cnt >= res:
                        continue
                if visited[nx][ny] == float('inf') or visited[nx][ny] >= tmp_cnt:
                    visited[nx][ny] = tmp_cnt
                    q.append([nx, ny, k, tmp_cnt])
    return res


if __name__ == '__main__':
    w, h = map(int, sys.stdin.readline().split())
    matrix = []
    c = []
    for i in range(h):
        matrix.append(list(sys.stdin.readline().rstrip()))
        for j, chr in enumerate(matrix[-1]):
            if chr == 'C':
                c.append([i,j])
    print(bfs(c, w, h))