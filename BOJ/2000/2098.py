import sys

def tsp(current, visited):
    if visited == (1<<n)-1:
        if dist[current][0] != 0:
            return dist[current][0]
        else:
            return float('inf')
    if dp[current][visited] != -1:
        return dp[current][visited]
    dp[current][visited]=float('inf')
    for next in range(n):
        if not(visited & (1<<next)) and dist[current][next]:
            dp[current][visited] = min(dp[current][visited], tsp(next, visited | (1<<next)) + dist[current][next])
    return dp[current][visited]

n = int(sys.stdin.readline())
dp = [[-1]*(1<<n) for _ in range(n)]
dist = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
print(tsp(0,1))