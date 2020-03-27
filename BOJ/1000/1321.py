import sys,bisect
n = int(sys.stdin.readline())
data = list(map(int,sys.stdin.readline().split()))
dp = [data[0]]
for i in range(1,n):
    dp.append(dp[i-1]+data[i])
M = int(sys.stdin.readline())
for _ in range(M):
    tmp = list(map(int,sys.stdin.readline().split()))
    if tmp[0] == 1:
        for i in range(tmp[1]-1,n):
            dp[i]+=tmp[2]
    elif tmp[0] == 2:
        print(bisect.bisect_left(dp,tmp[1])+1)