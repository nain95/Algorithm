import sys
n,k = map(int,sys.stdin.readline().split())
coin = [0]
dp = [0]*(k+1)
for _ in range(n):
    coin.append(int(sys.stdin.readline()))
dp[0] = 1
for i in range(1,n+1):
    for j in range(coin[i],k+1):
        dp[j] += dp[j-coin[i]]
print(dp[k])