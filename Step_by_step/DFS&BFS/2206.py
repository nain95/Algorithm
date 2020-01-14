import sys
from collections import deque
N,M = map(int,sys.stdin.readline().rstrip().split())
matrix = []
for i in range(N):
    matrix.append(list(map(int,list(sys.stdin.readline().rstrip()))))
visited = [[[0]*M for _ in range(N)] for _ in range(2)]
dx = [1,-1,0,0]
dy=[0,0,1,-1]
def bfs():
    queue = deque([[[0, 0, 0]]])
    visited[0][0][0] = 1
    exit = False
    cnt =0
    while 1:
        cnt += 1
        tmp = []
        nodes = queue.popleft()
        for node in nodes:
            x,y,b = node
            for i in range(4):
                nx,ny = x+dx[i],y+dy[i]
                if 0 <= nx < N and 0 <= ny < M:
                    if nx == N - 1 and ny == M - 1:
                        return cnt+1
                    if visited[b][nx][ny] == 0 and matrix[nx][ny] == 0:
                        tmp.append([nx,ny,b])
                        visited[b][nx][ny] = 1
                    elif visited[b][nx][ny] == 0 and matrix[nx][ny] == 1 and b==0:
                        tmp.append([nx,ny,1])
                        visited[b][nx][ny] = 1
        if tmp:
            queue.append(tmp)
        if not queue and visited[b][N-1][M-1] == 0:
            return -1
        if not queue:
            return cnt

print(bfs())
