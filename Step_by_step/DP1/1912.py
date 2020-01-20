import sys
N = int(sys.stdin.readline().rstrip())
data = list(map(int,sys.stdin.readline().rstrip().split()))
dp = [data[0]]
for i in range(0,N-1):
    dp.append(max(dp[i]+data[i+1],data[i+1]))
print(max(dp))