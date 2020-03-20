N = int(input())
data = [0]
for _ in range(N):
    data.append(int(input()))
if N == 1:
    print(data[1])
elif N == 2:
    print(data[1]+data[2])
elif N>=3:
    dp = [0,data[1],data[1]+data[2],max(data[2]+data[3],data[1]+data[3])]
    for i in range(4,N+1):
        dp.append(max(dp[i-2]+data[i],max(dp[0:i-2])+data[i-1]+data[i]))
    print(max(dp))
