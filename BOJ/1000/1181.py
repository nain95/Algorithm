import sys
N = int(sys.stdin.readline().rstrip())
data = []
for _ in range(N):
    data.append(sys.stdin.readline().rstrip())
data = list(set(data))
data = sorted(data, key= lambda x : (len(x),x))
for i in data:
    print(i)