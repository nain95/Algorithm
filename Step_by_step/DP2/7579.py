import sys
N,M = map(int,sys.stdin.readline().split())
app = list(map(int,sys.stdin.readline().split()))
mem = list(map(int,sys.stdin.readline().split()))
app_mem = []
for i in range(N):
    app_mem.append([app[i]*mem[i],app[i]])
app_mem.sort()
dp = [[0]*10001 for _ in range(N)]
dp[0][mem[0]] = app[0]
ans = sys.maxsize
for j in range(N):
    for z in range(10001):
        if z-mem[j] >= 0:
            dp[j][z] = max(dp[j][z],dp[j-1][z-mem[j]]+app[j])

        dp[j][z] = max(dp[j][z],dp[j-1][z])

        if dp[j][z] >= M:
            ans = (min(ans,z))
print(ans)