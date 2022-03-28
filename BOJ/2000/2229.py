import sys

n = int(sys.stdin.readline())
score = list(map(int, sys.stdin.readline().split()))
dp = [0] * n
for i in range(1, n):
    dp[i] = dp[i-1]
    for j in range(i-1, -1, -1):
        if j == 0:
            dp[i] = max(dp[i], max(score[j : i + 1]) - min(score[j : i + 1]))
        else:
            dp[i] = max(dp[i], dp[j-1] + max(score[j : i + 1]) - min(score[j : i + 1]))
print(dp[-1])