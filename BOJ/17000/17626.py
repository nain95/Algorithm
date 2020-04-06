import sys
n = int(sys.stdin.readline())
minnum = sys.maxsize
dp = [0]*50010
dp[1] = 1
stack = []
for i in range(1,230):
    stack.append(i*i)
for i in range(2,n+1):
    minnum = sys.maxsize
    j = 0
    while stack[j] <= i:
        tmp = i - stack[j]
        minnum = min(minnum,dp[tmp])
        j+=1
    dp[i] = minnum+1

print(dp[n])