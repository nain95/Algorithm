import sys

def check(S, E):
    if E - S == 1 or E - S == 2:
        if data[E] == data[S]:
            dp[S][E] = 1
            return 1
        else:
            dp[S][E] = 2
            return 2
    if dp[S][E] == 0:
        i = S+1
        j = E-1
        cnt = 0
        while i < j:
            dp[i][j] = check(i,j)
            if dp[i][j] != 1:
                cnt += 1
            i += 1
            j -= 1
        if cnt == 0 and data[S] == data[E]:
            dp[S][E] = 1
            return 1
        else:
            dp[S][E] = 2
            return 2
    else:
        return dp[S][E]


N = int(sys.stdin.readline())+1
data = [0]+list(map(int,sys.stdin.readline().split()))
M = int(sys.stdin.readline())
dp = [[0]*N for _ in range(N)]
for _ in range(M):
    S,E = map(int,sys.stdin.readline().split())
    if check(S,E) == 1:
        print(1)
    else:
        print(0)

