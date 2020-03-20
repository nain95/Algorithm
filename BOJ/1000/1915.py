import sys
n,m = map(int,sys.stdin.readline().split())
data = [[0]*(m+1)]
dp = [[0]*(m+1) for _ in range(n+1)]
for _ in range(n):
    data.append([0]+list(map(int,list(sys.stdin.readline().rstrip()))))
max_val = 0
for i in range(1,n+1):
    for j in range(1,m+1):
        if data[i][j] == 1:
            dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1]) + 1
            if dp[i][j] > max_val:
                max_val = dp[i][j]
result = pow(max_val,2)
print(result)