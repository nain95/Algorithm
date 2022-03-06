import sys

n = int(sys.stdin.readline())
matrix = []
dp = [[[0] * 3 for _ in range(n)] for _ in range(n)]
for _ in range(n):
    matrix.append(list(map(int, sys.stdin.readline().split())))
dp[0][1][0] = 1
for i in range(n):
    for j in range(1, n):
        if i == 0 and j == 1:
            continue
        if matrix[i][j] == 1:
            continue
        dp[i][j][0] = dp[i][j-1][0]
        if i == 0:
            continue
        else:
            dp[i][j][0] += dp[i][j-1][1]
            if matrix[i][j-1] != 1 and matrix[i-1][j] != 1:
                dp[i][j][1] += dp[i-1][j-1][0]
                dp[i][j][1] += dp[i-1][j-1][2]
                dp[i][j][1] += dp[i-1][j-1][1]
            dp[i][j][2] += dp[i-1][j][2]
            dp[i][j][2] += dp[i-1][j][1]
print(sum(dp[n-1][n-1]))
