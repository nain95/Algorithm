import sys

n = int(sys.stdin.readline())
for _ in range(n):
    M, N, x, y = map(int, sys.stdin.readline().split())
    num = x
    chk = (num-1) % N + 1
    cnt = 0
    while (num-1) % M + 1 != x or (num-1) % N + 1 != y:
        if cnt != 0 and (num-1) % N + 1 == chk:
            print(-1)
            break
        num += M
        cnt+=1
    else:
        print(num)
