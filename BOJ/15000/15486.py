import sys
N = int(sys.stdin.readline())
result = 0
dp = [0]*(N+2)
data = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
data.append([0,0])
for i in range(N + 1):
    result = max(result, dp[i])
    if i + data[i][0] > N:
        continue
    dp[i+data[i][0]] = max(result + data[i][1], dp[i+data[i][0]])
print(result)