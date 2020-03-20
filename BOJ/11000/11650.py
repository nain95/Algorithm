import sys
N = int(sys.stdin.readline().rstrip())
data = []
for _ in range(N):
    data.append(list(map(int,sys.stdin.readline().rstrip().split())))
data = sorted(data)
for i in data:
    print(i[0],end= ' ')
    print(i[1])