import sys
import bisect

def find(x):
    while x != node[x]:
        x = node[x]
        node[x] = node[node[x]]
    return x

def union(x,y):
    x = find(x)
    y = find(y)
    if x < y:
        node[x] = y
    else:
        node[y] = x

n, m, k = map(int, sys.stdin.readline().split())
card = sorted(list(map(int, sys.stdin.readline().split())))
node = {i:i for i in range(1, n+1)}
for num in list(map(int,sys.stdin.readline().split())):
    num = find(num)
    idx = bisect.bisect_right(card, num)
    tmp_num = card[idx]
    union(num, tmp_num)
    print(tmp_num)