import sys
n,k = map(int,sys.stdin.readline().split())
data = list(range(1,n+1))
index = 0
print('<',end = '')
for i in range(n):
    index = (index + (k-1))%len(data)
    result = data.pop(index)
    if i == n-1:
        print(result,end='')
    else:
        print(result, end=', ')
print('>')