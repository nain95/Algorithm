n = int(input())
dp = [0] * n
vip = []
t = int(input())
for _ in range(t):
    vip.append(int(input()) - 1)
dp[0] = 1
if 1 not in vip and 0 not in vip:
    dp[1] = 2
else:
    dp[1] = 1
for i in range(2, n):
    if i in vip or i-1 in vip:
        dp[i] = dp[i-1]
    else:
        dp[i] = dp[i-1] + dp[i-2]
print(dp[-1])