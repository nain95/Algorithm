import sys,bisect,itertools

def combinations(iterable, r):
    for i in range(N,M):
        print(dp)
        tmp = itertools.combinations(data[:i],N-1)
        for z in tmp:
            index = sum(z) % N
            if dp[index] == []:
                dp[index].append(list(z))
        print(dp)
        if data[i] == 0 and dp[0]:
            for res in dp[0][0]:
                print(res, end=' ')
            print(data[i])
            sys.exit()
        for j in range(N-data[i],len(dp),N):
            if dp[j]:
                for res in dp[j][0]:
                    print(res,end = ' ')
                print(data[i])
                sys.exit()
N = int(sys.stdin.readline())
M = 2 * N -1
data = list(map(int,sys.stdin.readline().split()))
dp = [[] for _ in range(N+2)]
if N == 1:
    print(data[0])
    sys.exit()
dp[sum(data[:N-1]) % N].append(data[:N-1])
#print(dp)
combinations(data,N-1)
print(-1)