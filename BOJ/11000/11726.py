import sys
n = int(sys.stdin.readline())
dp = [0,1,2]
for i in range(1,n-1):
    dp.append((dp[i]+dp[i+1])%10007)
print(dp[n])