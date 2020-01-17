T = int(input())
for _ in range(T):
    N = int(input())
    dp = [0, 1, 1, 1, 2, 2] + [0] * (N - 5)
    if N>=6:
        for i in range(6,N+1):
            dp[i] = dp[i-1]+dp[i-5]
    print(dp[N])
