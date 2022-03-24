import sys

n = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
dp = [0] * n
for idx, num in enumerate(data):
    if idx == 0:
        dp[0] = 1
    else:
        for j in range(idx-1, -1, -1):
            if num > data[j]:
                dp[idx] = max(dp[idx], dp[j])
        dp[idx] += 1
print(max(dp))
print(dp)