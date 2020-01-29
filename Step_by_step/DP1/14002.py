import sys
N = int(sys.stdin.readline().rstrip())
data = list(map(int,sys.stdin.readline().rstrip().split()))
dp = [1]+[0]*(N-1)
for i in range(1,len(data)):
    max_index = 0
    max_value = 0
    max_dp = 0
    cnt = 0
    for j in range(0,i):
        if data[j]<data[i]:
            if max_dp < dp[j]:
                max_value = data[j]
                max_index = j
                max_dp = dp[j]
            #elif max_value <= data[j] and dp[max_index] < dp[j]:
            #    max_value = data[j]
            #    max_index = j
            #    max_dp = dp[j]
        else:
            cnt+=1
    if cnt == i:
        max_index = i
    dp[i] = dp[max_index]+1
stack = []
result = max(dp)
print(result)
for i in range(N-1,-1,-1):
    if dp[i] == result:
        stack.append(data[i])
        result-=1
for _ in range(len(stack)):
    print(stack.pop(),end=' ')


