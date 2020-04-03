import sys
def getnum():
    for i in range(n+1):
        if numdata[i] != 0 :
            return i
    return -1
n,k = map(int,sys.stdin.readline().split())
numdata = [0,0]+[1] * (n-1)
cnt = 0
i = getnum()
while i != -1:
    j = i
    while j <= n:
        if numdata[j] == 1:
            numdata[j] = 0
            cnt += 1
            if cnt == k:
                print(j)
                sys.exit()
        j += i
    i = getnum()