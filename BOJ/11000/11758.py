import sys

def ccw(a, b, c):
    x1, y1, x2, y2, x3, y3 = a + b + c
    ans = (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)
    if ans < 0:
        return -1
    elif ans > 0:
        return 1
    else:
        return 0

a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))
c = list(map(int, sys.stdin.readline().split()))
print(ccw(a,b,c))