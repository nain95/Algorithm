import sys
N = int(sys.stdin.readline())
data = []
result = 0
dp = [0]*(N+1)
for _ in range(N):
    data.append(list(map(int,sys.stdin.readline().split())))
for i in range(N+1):
    for j in range(i):
        dp[i] = max(dp[i],dp[j])
        if j +data[j][0] == i:
            dp[i] = max(dp[i],dp[j]+data[j][1])
    result = max(result,dp[i])
print(result)