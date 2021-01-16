import sys
from collections import defaultdict

def solve(n):
    dp[1] = 0
    for i in range(2,n+1):
        dp[i] = dp[i-1] + 1
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i/2] + 1)
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i/3] + 1)

a = int(sys.stdin.readline())
dp = defaultdict(int)
solve(a)
print(dp[a])