import sys
N,M = list(map(int,sys.stdin.readline().rstrip().split()))
matrix = []
matrix_check = [[0]*M for _ in range(N)]
cnt = [[0]*M for _ in range(N)]
for _ in range(N):
    matrix.append(list(map(int,list(sys.stdin.readline().rstrip()))))
dx = [1,-1,0,0]
dy = [0,0,1,-1]
def bfs():
    result = []
    matrix_check[0][0] = 1
    cnt[0][0] = 1
    queue = []
    queue.append([0,0])
    while queue != []:
        x,y = queue.pop(0)
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if matrix_check[nx][ny] == 0 and matrix[nx][ny]==1:
                    queue.append([nx,ny])
                    cnt[nx][ny] = cnt[x][y]+1
                    matrix_check[nx][ny]=1
    print(cnt[N-1][M-1])
bfs()