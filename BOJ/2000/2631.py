import sys

n = int(sys.stdin.readline())
dp = [1] * n
data = []
for i in range(n):
    num = int(sys.stdin.readline())
    data.append(num)
    for j in range(i):
        if data[i] > data[j]:
            dp[i] = max(dp[i], dp[j] + 1)
print(n - max(dp))
