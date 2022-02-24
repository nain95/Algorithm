import sys
from collections import defaultdict

def ccw(a, b, c):
    x1, y1, x2, y2, x3, y3 = a + b + c
    ans = (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)
    if ans < 0:
        return -1
    elif ans > 0:
        return 1
    else:
        return 0

def line_cross_discrimination(a_line: list, b_line: list):
    a = a_line[:2]
    b = a_line[2:]
    c = b_line[:2]
    d = b_line[2:]
    ccw_res1 = ccw(a, b, c)
    ccw_res2 = ccw(a, b, d)
    ccw_res3 = ccw(c, d, a)
    ccw_res4 = ccw(c, d, b)
    ccw_mul_res1 = ccw_res1 * ccw_res2
    ccw_mul_res2 = ccw_res3 * ccw_res4
    if ccw_mul_res1 == 0:
        if ccw_res1 != 0:
            ccw_mul_res1 = -1
        elif ccw_res2 != 0:
            ccw_mul_res1 = -1
    if ccw_mul_res2 == 0:
        if ccw_res3 != 0:
            ccw_mul_res2 = -1
        elif ccw_res4 != 0:
            ccw_mul_res2 = -1
    if a == c or a == d or b == c or b == d:
        return 1
    if ccw_mul_res1 < 0 and ccw_mul_res2 < 0:
        return 1
    if ccw_mul_res1 == 0 and ccw_mul_res2 == 0:
        if a[0] > b[0]:
            a, b = b, a
        if c[0] > d[0]:
            c, d = d, c
        if a[0] == b[0]:
            if a[1] <= d[1] and c[1] <= b[1]:
                return 1
        elif a[1] == b[1]:
            if a[0] <= d[0] and c[0] <= b[0]:
                return 1
        elif compare_crd(a, b, c, d):
            return 1
    return 0

def compare_crd(a, b, c, d):
    if a[1] < b[1]:
        return a[1] <= d[1] and c[1] <= b[1]
    else:
        return a[1] >= d[1] and c[1] >= b[1]
    
def find_parent(parent, x):
    if x == parent[x]:
        return x
    else:
        y = find_parent(parent, parent[x])
        parent[x] = y
        return y

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a == b:
        return
    parent[b] = a

cnt = int(sys.stdin.readline())
parent = [0] * (cnt)
line_list = []
for line_num in range(cnt):
    line_list.append(list(map(int, sys.stdin.readline().split())))
    parent[line_num] = line_num
for x in range(cnt - 1):
    for y in range(x+1, cnt):
        if line_cross_discrimination(line_list[x], line_list[y]) == 1:
            union_parent(parent, x, y)
for i in range(cnt):
    find_parent(parent, i)
dic = defaultdict(int)
for i in range(cnt):
    dic[parent[i]] += 1
print(len(dic))
print(max(dic.values()))