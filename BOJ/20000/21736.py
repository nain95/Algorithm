import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
matrix = []
start = [0, 0]
for i in range(n):
    matrix.append(list(sys.stdin.readline()))
    if 'I' in matrix[-1]:
        for j in range(m):
            if matrix[i][j] == 'I':
                start = [i, j]

nx, ny = [0, 0, 1, -1], [1, -1, 0, 0]
queue = deque([start])
ans = 0
visited = [[0] * m for _ in range(n)]
while queue:
    x, y = queue.popleft()
    for k in range(4):
        kx, ky = x + nx[k], y + ny[k]
        if 0 <= kx < n and 0 <= ky < m and visited[kx][ky] == 0 and matrix[kx][ky] != "X":
            if matrix[kx][ky] == 'P':
                ans += 1
            visited[kx][ky] = 1
            queue.append([kx, ky])
print(ans if ans != 0 else "TT")
