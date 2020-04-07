import sys
n = int(sys.stdin.readline())
dp = [0,1,3]
for i in range(1,n-1):
    dp.append((dp[i]*2+dp[i+1])%10007)
print(dp[n])