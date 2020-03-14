import sys,itertools
n,m = map(int,sys.stdin.readline().split())
data = list(map(int,sys.stdin.readline().rstrip().split()))
data.sort()
result = itertools.permutations(data,m)
for i in result:
    for j in i:
        print(j,end=' ')
    print()