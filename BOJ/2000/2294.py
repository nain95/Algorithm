import sys

n, k = map(int, sys.stdin.readline().split())
coin = []
for _ in range(n):
    coin.append(int(sys.stdin.readline()))
dp = [float('inf')] * (k+1)
dp[0] = 0
for i in range(n):
    for j in range(coin[i], k + 1):
        dp[j] = min(dp[j], dp[j - coin[i]] + 1)
print(dp[-1] if dp[-1] != float('inf') else -1)