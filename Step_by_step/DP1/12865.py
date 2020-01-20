import sys
N,K = map(int,sys.stdin.readline().rstrip().split())
wl = []
vl = []
for _ in range(N):
    w,v = map(int,sys.stdin.readline().rstrip().split())
    wl.append(w)
    vl.append(v)
dp = [[0 for x in range(K+1)] for x in range(N+1)]
for i in range(1,N+1):
    for j in range(1,K+1):
        if j < wl[i-1]:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(vl[i - 1] + dp[i - 1][j - wl[i - 1]], dp[i - 1][j])

print(dp[N][K])