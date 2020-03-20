import sys,math

def mininit(node, start, end):
    if start == end :
        mintree[node] = data[start]
        return mintree[node]
    else:
        mintree[node] = min(mininit(node*2, start, (start+end)//2) , mininit(node*2+1, (start+end)//2+1, end))
        return mintree[node]

def maxinit(node, start, end):
    if start == end :
        maxtree[node] = data[start]
        return maxtree[node]
    else:
        maxtree[node] = max(maxinit(node*2, start, (start+end)//2) , maxinit(node*2+1, (start+end)//2+1, end))
        return maxtree[node]


def minget(node,start,end,left,right):
    if left > end or right < start:
        return sys.maxsize
    elif left <= start and right >= end:
        return mintree[node]

    return min(minget(node * 2, start ,(start+end)//2,left,right) , minget(node*2 + 1, (start+end)//2+1, end, left, right))


def maxget(node,start,end,left,right):
    if left > end or right < start:
        return 0
    elif left<=start and right >= end:
        return maxtree[node]

    return max(maxget(node * 2, start ,(start+end)//2,left,right) , maxget(node*2 + 1, (start+end)//2+1, end, left, right))

n,m = map(int,sys.stdin.readline().split())
height = math.ceil(math.log(n) / math.log(2))
S = int(math.pow(2,height))
mintree = [0] * (S*2)
maxtree = [0] * (S*2)
data = []
for _ in range(n):
    data.append(int(sys.stdin.readline()))
    
mininit(1,0,n-1)
maxinit(1,0,n-1)
for _ in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    print(minget(1,0,n-1,a-1,b-1),end = ' ')
    print(maxget(1, 0, n - 1, a - 1, b - 1))
