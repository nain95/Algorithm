import sys
t = int(sys.stdin.readline())
for _ in range(t):
    ans = 0
    n,m = map(int,sys.stdin.readline().split())
    book = []
    for i in range(1,n+1):
        book.append(1)
    ab = []
    for _ in range(m):
        ab.append(list(map(int,sys.stdin.readline().split())))
    ab = sorted(ab,key=lambda x:x[1])
    for tmp in ab:
        for i in range(tmp[0],tmp[1]+1):
            if book[i-1] == 1:
                ans+=1
                book[i-1] = 0
                break
    print(ans)