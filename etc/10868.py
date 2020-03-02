import sys, math

def mininit(node, start, end):
    if start == end:
        mintree[node] = data[start]
        return mintree[node]

    mintree[node] = min(mininit(node * 2, start, (start + end) // 2),mininit(node * 2 + 1, (start + end) // 2 + 1, end))
    return mintree[node]

def minget(node, start, end, left, right):
    if left > end or right < start:
        return sys.maxsize
    elif left <= start and right >= end:
        return mintree[node]

    return min(minget(node * 2, start, (start + end) // 2, left, right),
               minget(node * 2 + 1, (start + end) // 2 + 1, end, left, right))

mintree=[0 for i in range(3000000)]
data=[]
n,m=map(int,sys.stdin.readline().split())

for _ in range(n):
    data.append(int(sys.stdin.readline()))

mininit(1,0,n-1)

for _ in range(m):
    a,b = map(int,sys.stdin.readline().split())
    print(minget(1,0,n-1,a-1,b-1))