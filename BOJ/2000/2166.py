import sys

def ccw(a, b, c):
    x1, y1, x2, y2, x3, y3 = a + b + c
    ans = (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)
    return ans

n = int(sys.stdin.readline())
ans = 0
line_list = []
for _ in range(n):
    line_list.append(list(map(int, sys.stdin.readline().split())))
for i in range(1, n-1):
    ans += ccw(line_list[0], line_list[i], line_list[i+1]) / 2.0
print(round(abs(ans), 1))
