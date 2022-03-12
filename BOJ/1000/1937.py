import sys

def dfs(x, y):
    if dp[x][y]:
        return dp[x][y]
    dp[x][y] = 1
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < n and 0 <= ny < n and matrix[x][y] < matrix[nx][ny]:
            dp[x][y] = max(dp[x][y], dfs(nx, ny) + 1)
    return dp[x][y]

n = int(sys.stdin.readline())
matrix = []
dp = [[0] * n for _ in range(n)]
dx, dy = (1, -1, 0, 0), (0, 0, 1, -1)
for _ in range(n):
    matrix.append(list(map(int, sys.stdin.readline().split())))
ans = 0
for x in range(n):
    for y in range(n):
        ans = max(ans, dfs(x, y))
print(ans)