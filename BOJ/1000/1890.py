import sys

n = int(sys.stdin.readline())
matrix = []
dp = [[0] * n for _ in range(n)]
dp[0][0] = 1
for _ in range(n):
    matrix.append(list(map(int, sys.stdin.readline().split())))
for i in range(n):
    for j in range(n):
        if dp[i][j] == 0 or matrix[i][j] == 0:
            continue
        dist = matrix[i][j]
        down = dist + i
        right = dist + j

        if down < n:
            dp[down][j] += dp[i][j]
        if right < n:
            dp[i][right] += dp[i][j]
print(dp[i][j])