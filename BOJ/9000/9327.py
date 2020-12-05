import sys
T = int(sys.stdin.readline())
for _ in range(T):
    N,M = map(int,sys.stdin.readline().split())
    app = [0]+list(map(int,sys.stdin.readline().split()))
    dp = [[1000000000]*(M+1) for _ in range(N+1)]
    ans = sys.maxsize
    chk = False
    if N == 1:
        if app[1] * 2 >= M:
            print(app[1])
        else:
            print("FULL")
        continue
    dp[0][app[1]] = app[1]*2
    for j in range(N+1):
        for z in range(M+1):
            if app[j] * 2 >= z:
                if dp[j-1][z] + app[j] * 2 >= z:
                    dp[j][z] = min(dp[j-1][z],dp[j-1][z] + app[j])
                else:
                    dp[j][z] = dp[j-1][z]
            else:
                dp[j][z] = dp[j-1][z]
    print(dp)
            #if dp[j][z] * 2 >= M:
            #    ans = min(ans,dp[j][z])
            #    chk = True
    if chk:
        print(ans)
    else:
        print("FULL")