import sys
N = int(sys.stdin.readline().rstrip())
data = [0]*10001
for _ in range(N):
    data[int(sys.stdin.readline().rstrip())] += 1
cnt = 0
for i in range(10001):
    while data[i] > 0:
        sys.stdout.write(str(i)+'\n')
        data[i] -= 1
