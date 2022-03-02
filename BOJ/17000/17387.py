import sys

def ccw(a, b, c):
    x1, y1, x2, y2, x3, y3 = a + b + c
    return (x1 * y2 + x2 * y3 + x3 * y1) - (x2 * y1 + x3 * y2 + x1 * y3)

x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
x3, y3, x4, y4 = map(int, sys.stdin.readline().split())
a = (x1, y1)
b = (x2, y2)
c = (x3, y3)
d = (x4, y4)
if a > b:
    a, b = b, a
if c > d:
    c, d = d, c
ccw_res1 = ccw(a, b, c) * ccw(a, b, d)
ccw_res2 = ccw(c, d, a) * ccw(c, d, b)
ccw_res = ccw_res1 * ccw_res2
if ccw_res1 == 0 and ccw_res2 == 0:
    if a <= d and c <= b:
        ans = 1
    else:
        ans = 0
elif ccw_res1 <= 0 and ccw_res2 <= 0:
    ans = 1
else:
    ans = 0
print(ans)
