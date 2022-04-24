import sys
import heapq
from collections import defaultdict

ans = 0
n = int(sys.stdin.readline())
pos_list = [list(map(int, sys.stdin.readline().split()))+[0]]
for i in range(n-1):
    pos_list.append(list(map(int, sys.stdin.readline().split())) + [i+1])
dic = defaultdict(dict)
for i in range(3):
    sorted_list = sorted(pos_list, key=lambda x:x[i])
    for j in range(n-1):
        a = sorted_list[j][3]
        b = sorted_list[j + 1][3]
        if b in dic[a]:
            dic[a][b] = min(dic[a][b], abs(pos_list[a][i]-pos_list[b][i]))
        else:
            dic[a][b] = abs(pos_list[a][i]-pos_list[b][i])
        if a in dic[b]:
            dic[b][a] = min(dic[b][a], abs(pos_list[a][i]-pos_list[b][i]))
        else:
            dic[b][a] = abs(pos_list[a][i]-pos_list[b][i])
visited = 0
heap = [(0,list(dic.keys())[0])]
while heap:
    cost, key = heapq.heappop(heap)
    if visited & (1 << key) != 0:
        continue
    ans += cost
    visited |= 1 << key
    for k in dic[key].keys():
        c = dic[key][k]
        if visited & (1 << k) == 0:
            heapq.heappush(heap,(c, k))
print(ans)