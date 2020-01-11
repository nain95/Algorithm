import sys
N = int(sys.stdin.readline().rstrip())
time = list(map(int,sys.stdin.readline().rstrip().split()))
time = sorted(time)
result = 0
tmp = 0
for i in time:
    tmp += + i
    result += tmp
print(result)