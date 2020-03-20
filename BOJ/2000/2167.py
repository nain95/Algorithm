import sys
n,m = map(int,sys.stdin.readline().split())
matrix = []
for _ in range(n):
    matrix.append(list(map(int,sys.stdin.readline().split())))
K = int(sys.stdin.readline())
for _ in range(K):
    result = 0
    i,j,x,y = map(int,sys.stdin.readline().split())
    for l in range(i-1,x):
        for z in range(j-1,y):
            result+=matrix[l][z]
    print(result)

