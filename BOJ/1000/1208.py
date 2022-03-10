import sys
from collections import defaultdict
from itertools import combinations

n, s = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))
a, b = data[:n//2], data[n//2:]
a_dic, b_dic = defaultdict(int), defaultdict(int)
for i in range(1, max(len(b), len(a)) + 1):
    if i <= len(a):
        for num in combinations(a, i):
            a_dic[sum(num)] += 1 
    if i <= len(b):
        for num in combinations(b, i):
            b_dic[sum(num)] += 1
ans = 0
for a_num in a_dic.keys():
    if s - a_num in b_dic:
        ans += b_dic[s - a_num] * a_dic[a_num]
print(ans + a_dic[s] + b_dic[s])