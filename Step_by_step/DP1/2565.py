import sys
N = int(sys.stdin.readline().rstrip())
data = []
for _ in range(N):
    data.append(list(map(int,sys.stdin.readline().rstrip().split())))
dp = [0]*N
sort_data = sorted(data, key = lambda x : x[0])
dp[0] = 1
for i in range(1,N):
    max_index = 0
    max_value = 0
    max_dp = 0
    cnt = 0
    for j in range(0,i):
        if sort_data[j][1]<sort_data[i][1]:
            if max_dp < dp[j]:
                max_value = sort_data[j][1]
                max_index = j
                max_dp = dp[j]
        else:
            cnt+=1
    if cnt == i:
        max_index = i
    dp[i] = dp[max_index]+1

print(N-max(dp))