import sys
n,m,b = map(int,sys.stdin.readline().split())
data = []
for _ in range(n):
    tmp = list(map(int,sys.stdin.readline().split()))
    for i in tmp:
        data.append(i)
mindata = min(data)
maxdata = max(data)
result = sys.maxsize
for i in range(mindata,maxdata+1):
    cnt = 0
    back = b
    for j in data:
        if i == j:
            continue
        if i > j:
            cnt += i-j
            back -= i-j
        else:
            cnt += (j-i)*2
            back += (j-i)
    if back >= 0:
        if result >= cnt:
            result = cnt
            height = i
print(result,height)
