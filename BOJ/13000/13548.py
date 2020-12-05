import sys
n = int(sys.stdin.readline())
an = list(map(int,sys.stdin.readline().split()))
m = int(sys.stdin.readline())
data = [0]*(n+1)
for z in an:
    data[z] += 1
print(data)
for _ in range(m):
    i,j = map(int,sys.stdin.readline().split())
    print(max(data[i:j+1]))