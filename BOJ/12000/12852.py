import sys
from collections import defaultdict

def solve(n):
    dp[1] = 0
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + 1
        dp_path[i] = i - 1
        if i % 2 == 0:
            if dp[i] > dp[i / 2] + 1:
                dp[i] = dp[i / 2] + 1
                dp_path[i] = i // 2
        if i % 3 == 0:
            if dp[i] > dp[i / 3] + 1:
                dp[i] = dp[i / 3] + 1
                dp_path[i] = i // 3

a = int(sys.stdin.readline())
dp = defaultdict(int)
dp_path = {}
solve(a)
print(dp[a])
print(a, end= ' ')
while a != 1:
    print(dp_path[a], end=' ')
    a = dp_path[a]
