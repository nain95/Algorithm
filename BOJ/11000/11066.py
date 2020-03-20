import sys
t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    data = list(map(int,sys.stdin.readline().split()))
    sum = [0]
    for i in range(len(data)):
        sum.append(sum[i]+data[i])
    dp = [[0]*(n+1) for _ in range(n+1)]
    for i in range(1,n):
        for j in range(1,n-i+1):
            z = i+j
            dp[j][z] = sys.maxsize
            for mid in range(j,z):
                dp[j][z] = min(dp[j][z],dp[j][mid]+dp[mid+1][z] + sum[z] - sum[j-1])
    print(dp[1][n])
    for q in dp:
        print(q)  