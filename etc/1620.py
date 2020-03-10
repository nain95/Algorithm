import sys
N,M = map(int,sys.stdin.readline().split())
data = {}
for i in range(N):
    data[sys.stdin.readline().rstrip()] = i+1
for _ in range(M):
    tmp = sys.stdin.readline().rstrip()
    if tmp in data:
        print(data[tmp])
    else:
        tmp = int(tmp)
        chk = 0
        for i in data:
            chk+=1
            if chk == tmp:
                print(i)
                break