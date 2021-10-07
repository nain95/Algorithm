import sys
from collections import defaultdict, deque

def dfs(start, cur, distance, visited):
    global leaf
    visited[cur] = 1
    ck = 0
    for node in dic[cur]:
        if visited[node] == -1:
            dist_dic[start][node] = dist_dic[cur][node] + distance
            dfs(start, node, distance + dist_dic[cur][node], visited)
            ck = 1
    if ck == 0 and leaf[1] < dist_dic[start][cur]:
        leaf = [cur, dist_dic[start][cur]]
        

v = int(sys.stdin.readline())
dic = defaultdict(list)
dist_dic = defaultdict(dict)
for _ in range(v):
    data = list(map(int, sys.stdin.readline().split()))
    for idx in range(1, len(data), 2):
        if data[idx] == -1:
            break
        dic[data[0]].append(data[idx])
        dist_dic[data[0]][data[idx]] = data[idx + 1]
        dist_dic[data[idx]][data[0]] = data[idx + 1]
leaf = [0,0]
dfs(1, 1, 0, [-1] * (v + 1))
leaf[1] = -1
dfs(leaf[0], leaf[0], 0, [-1] * (v + 1))
print(leaf[1])