import sys
n = int(sys.stdin.readline())
data = list(map(int,sys.stdin.readline().split()))
data = sorted(data)
print(data[0]*data[-1])
