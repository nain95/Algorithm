import sys
T = int(sys.stdin.readline())
for _ in range(T):
    H,W,N = map(int,sys.stdin.readline().split())
    tmp1 = (N%H)*100
    tmp2 = (N//H)+1
    if tmp1 == 0:
        tmp1 = H*100
        tmp2 = (N//H)
    print(tmp1+tmp2)