import sys

n = int(sys.stdin.readline())
p = list(map(int,[0] + sys.stdin.readline().split()))
dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
answer = 0
dp[1] = [0] + [p[1] * i for i in range(1, n+1)]
for i in range(2, n + 1):
    for j in range(1, n + 1):
        if j < i:
            dp[i][j] = dp[i-1][j]
        elif i == j:
            dp[i][j] = max(p[i], dp[i-1][j])
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j-i] + p[i])
    answer = max(answer, dp[i][j])
print(answer)
