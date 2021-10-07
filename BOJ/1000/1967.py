import sys
from collections import defaultdict, deque
sys.setrecursionlimit(10**6)

def dfs(start, cur, distance):
    global leaf
    ck = 0
    for node in dic[cur]:
    
        dist_dic[min(node,start)][max(node,start)] = dist_dic[min(cur,node)][max(cur,node)] + distance
        dfs(start, node, distance + dist_dic[min(cur,node)][max(cur,node)])
        ck = 1 
    if ck == 0 and leaf[1] < dist_dic[min(start,cur)][max(start,cur)]:
        leaf = [cur, dist_dic[min(start,cur)][max(start,cur)]]

v = int(sys.stdin.readline())
dic = defaultdict(list)
dist_dic = defaultdict(dict)
for i in range(1,v+1):
    dist_dic[i][i] = 0
for _ in range(v-1):
    parents, children, dist = map(int, sys.stdin.readline().split())
    dic[parents].append(children)
    dic[children].append(parents)
    dist_dic[min(parents,children)][max(parents,children)] = dist
leaf = [0,0]
dfs(1, 1, 0)
print(dic[1])
print(dist_dic[1])
leaf[1] = -1
dfs(leaf[0], leaf[0], 0)
print(sys.getsizeof(dic))
