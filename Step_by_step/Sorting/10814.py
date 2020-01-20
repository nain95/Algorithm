import sys
N = int(sys.stdin.readline().rstrip())
data = []
for _ in range(N):
    data.append(sys.stdin.readline().rstrip().split())
data = sorted(data,key = lambda x:int(x[0]))
for i in data:
    print(i[0],end= ' ')
    print(i[1])