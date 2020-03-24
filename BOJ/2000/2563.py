import sys
n = int(sys.stdin.readline())
data = [[0]*100 for _ in range(100)]
result = 0
for _ in range(n):
    x,y = map(int,sys.stdin.readline().split())
    for i in range(10):
        for j in range(10):
            data[x+i][y+j] = 1
for i in range(100):
    for j in range(100):
        if data[i][j] == 1:
            result+=1
print(result)