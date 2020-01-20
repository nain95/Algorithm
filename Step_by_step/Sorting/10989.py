import sys
N = int(sys.stdin.readline().rstrip())
data = [0]*10001
for _ in range(N):
    tmp = int(sys.stdin.readline().rstrip())
    data[tmp] += 1
cnt = 0
for i in range(10001):
    print('%d\n'%i*data[i],end='')
