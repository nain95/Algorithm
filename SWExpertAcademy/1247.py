def distance(start,end):
    return abs(data[start][0] - data[end][0]) + abs(data[start][1] - data[end][1])


def tsp(current,visited):
    if visited == ((1 << n) -1) ^ (1 << (n-1)):
        return abs(data[current][0]-data[-1][0]) + abs(data[current][1]-data[-1][1])
    if dp[current][visited] != -1:
        return dp[current][visited]
    dp[current][visited] = float('inf')
    for next in range(1,n):
        if not (visited & (1 << next)):
            dp[current][visited] = min(dp[current][visited], tsp(next, visited | (1 << next)) + distance(current,next))
    return dp[current][visited]


T = int(input())
for case in range(T):
    n = int(input())+2
    input_data = list(map(int,input().split()))
    home = [input_data[0:2]]
    company = [input_data[2:4]]
    customer = [input_data[i:i+2] for i in range(4,len(input_data),2)]
    data = home + customer + company
    print(data)
    dp = [[-1]*(1<<(n+2)) for _ in range(n+2)]
    print(f'#{case+1} {tsp(0,1)}')