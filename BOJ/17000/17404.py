import sys

n = int(sys.stdin.readline())
cost = []
dp = [[[float('inf')] * 3 for _ in range(n)] for _ in range(3)]
for _ in range(n):
    cost.append(list(map(int, sys.stdin.readline().split())))
dp[0][0][0] = cost[0][0]
dp[1][0][1] = cost[0][1]
dp[2][0][2] = cost[0][2]
for i in range(1, n):
    if i != n-1:
        for j in range(3):
            for a, b, c in [(0, 1, 2), (1, 2, 0), (2, 1, 0)]:
                dp[j][i][a] = min(dp[j][i-1][b] + cost[i][a], dp[j][i-1][c] + cost[i][a])
    else:
        dp[1][i][0] = min(dp[1][i-1][1] + cost[i][0], dp[1][i-1][2] + cost[i][0])
        dp[2][i][0] = min(dp[2][i-1][1] + cost[i][0], dp[2][i-1][2] + cost[i][0])
        dp[0][i][1] = min(dp[0][i-1][0] + cost[i][1], dp[0][i-1][2] + cost[i][1])
        dp[2][i][1] = min(dp[2][i-1][0] + cost[i][1], dp[2][i-1][2] + cost[i][1])
        dp[0][i][2] = min(dp[0][i-1][0] + cost[i][2], dp[0][i-1][1] + cost[i][2])
        dp[1][i][2] = min(dp[1][i-1][0] + cost[i][2], dp[1][i-1][1] + cost[i][2])
        print(min(dp[1][i][0], dp[2][i][0], dp[0][i][1], dp[2][i][1], dp[0][i][2], dp[1][i][2]))