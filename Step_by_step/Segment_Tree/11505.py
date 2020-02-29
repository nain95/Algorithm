import sys


def init(node, start, end):
    if start == end :
        tree[node] = l[start]% 1000000007
    else:
        half = (start + end) // 2
        init(node * 2, start, half);
        init(node * 2 + 1, half + 1, end);
        tree[node] = (tree[node * 2] * tree[node * 2 + 1]) % 1000000007;



def subSum(node,start,end,left,right):
    if left > end or right < start:
        return -1

    if left <= start and end <= right:
        return tree[node]

    m1 = subSum(node * 2, start ,(start+end)//2,left,right)
    m2 = subSum(node*2 + 1, (start+end)//2+1, end, left, right)
    if m1 == -1:
        return m2
    elif m2 == -1:
        return m1
    else:
        return (m1*m2) %1000000007


def update(node, start, end, index, diff):
    if index < start or index > end:
        return
    if start == end:
        tree[node] = diff % 1000000007
    else:
        update(node * 2, start, (start + end) // 2, index, diff)
        update(node * 2 + 1, (start + end) // 2 + 1, end, index, diff)

        tree[node] = (tree[node * 2] * tree[node * 2 + 1]) % 1000000007;



n, m, k = map(int,sys.stdin.readline().split())

l = [0] * 3000000
tree = [0] * 3000000

for i in range(n):
    l[i]=int(sys.stdin.readline())

init(1,0,n-1)
for _ in range(m + k):
    a, b, c = map(int, input().rstrip().split())

    if a == 1:
        update(1, 0, n - 1, b-1, c)
        l[b-1] = c
    elif a == 2:
        print(subSum(1, 0, n - 1, b - 1, c - 1))