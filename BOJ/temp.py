import sys,bisect,itertools,random,time

def combinations(iterable, r):
    past = -1
    for i in range(N,M):
        if past == 0 and data[i] == 0:
            continue
        #print(dp)
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
            print(time.time()-start)
            sys.exit()
        for j in range(N-data[i],len(dp),N):
            if dp[j]:
                for res in dp[j][0]:
                    print(res,end = ' ')
                print(data[i])
                print(time.time()-start)
                sys.exit()
        past = data[i]
        #print(dp)
N = int(sys.stdin.readline())
start = time.time()
M = 2 * N -1
data = []
for j in range(N//2):
    data.append(1)
for j in range(N//2,N):
    data.append(0)
for j in range(N,M):
    data.append(1)
print(data)
dp = [[] for _ in range(N+2)]
if N == 1:
    print(data[0])
    sys.exit()
dp[sum(data[:N-1]) % N].append(data[:N-1])
#print(dp)
combinations(data,N-1)
print(-1)
print(time.time()-start)