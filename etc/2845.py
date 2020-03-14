import sys
l,p = map(int,sys.stdin.readline().split())
data = list(map(int,sys.stdin.readline().split()))
for i in data:
    print(i-l*p,end=' ')