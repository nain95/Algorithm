import sys
N,M = map(int,sys.stdin.readline().rstrip().split())
tmp = list(map(int,sys.stdin.readline().rstrip().split()))
dp = [0,tmp[0]]
for i in range(1,N):
    dp.append(dp[i]+tmp[i])
for _ in range(M):
    start, end = map(int,sys.stdin.readline().rstrip().split())
    if start == 1 :
        print(dp[end])
    else:
        print(dp[end]-dp[start-1])