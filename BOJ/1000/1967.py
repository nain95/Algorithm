import sys
from collections import defaultdict, deque
sys.setrecursionlimit(10**6)

def dfs(start, cur, distance, tmp):
    global leaf
    ck = 0
    for node in dic[cur].keys():
        if node != tmp:
            dfs(start, node, distance + dic[min(cur,node)][max(cur,node)], cur)
            ck = 1 
    if ck == 0 and leaf[1] < distance:
        leaf = [cur, distance]

v = int(sys.stdin.readline())
dic = defaultdict(dict)
for _ in range(v-1):
    parents, children, dist = sys.stdin.readline().split()
    dist = int(dist)
    dic[parents][children] = dist
    dic[children][parents] = dist
leaf = ['0',0]
dfs('1', '1', 0, '1')
leaf[1] = -1
dfs(leaf[0], leaf[0], 0, leaf[0])
print(leaf[1])