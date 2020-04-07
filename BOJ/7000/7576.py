import sys
from collections import deque

def bfs():
    cnt = 0
    check = [[False]*(M) for _ in range(N)]
    while queue:
        nodes = queue.pop(0)
        tmp = []
        for node in nodes:
            x,y = node
            check[x][y] = True
            for i in range(4):
                nx,ny=x+dx[i],y+dy[i]
                if 0 <= nx < N and 0 <= ny < M:
                    if matrix[nx][ny] == 0 and check[nx][ny] == False:
                        matrix[nx][ny] = 1
                        tmp.append([nx,ny])
                    check[nx][ny] = True
        if tmp:
            cnt+=1
            queue.append(tmp)
    for row in matrix:
        if 0 in row:
            return -1
    return cnt

M,N = list(map(int,sys.stdin.readline().rstrip().split()))
matrix=[]
queue = []
result = 0
dx = [1,-1,0,0]
dy = [0,0,1,-1]

for i in range(N):
    tmp = list(map(int,sys.stdin.readline().rstrip().split()))
    matrix.append(tmp)
    for j in range(M):
        if tmp[j] == 1:
            queue.append([i,j])
queue = [queue]
print(bfs())
