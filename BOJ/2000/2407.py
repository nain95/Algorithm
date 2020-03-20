import sys
n,r = map(int,sys.stdin.readline().split())
a = 1
b = 1
for i in range(r):
    a *= n-i
for j in range(r):
    b *= (r-j)
print(a//b)