from collections import deque
import sys

n = int(sys.stdin.readline())
for _ in range(n):
    l = int(sys.stdin.readline())
    a, b = map(int, sys.stdin.readline().split())
    c, d = map(int, sys.stdin.readline().split())
    dx, dy = (-2, -2, -1, 1, 2, 2, 1, -1), (-1, 1, 2, 2, 1, -1, -2, -2)
    queue = deque([[a, b]])
    visited = [[-1] * l for _ in range(l)]
    ans = -1
    while queue:
        length = len(queue)
        ans += 1
        for _ in range(length):
            x, y = queue.popleft()
            if [x,y] == [c,d]:
                break
            visited[x][y] = 1
            for k in range(8):
                nx, ny = x + dx[k], y + dy[k]
                if 0 <= nx < l and 0 <= ny < l and visited[nx][ny] == -1:
                    queue.append([nx, ny])
                    visited[nx][ny] = 1
        else:
            continue
        break
    print(ans)