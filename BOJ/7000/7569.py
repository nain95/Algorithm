import sys

def bfs():
    cnt = 0
    while queue:
        nodes = queue.pop(0)
        tmp = []
        for node in nodes:
            h,x,y = node
            check[h][x][y] = True
            for i in range(4):
                nx,ny=x+dx[i],y+dy[i]
                if 0 <= nx < N and 0 <= ny < M:
                    if matrix[h][nx][ny] == 0 and check[h][nx][ny] == False:
                        matrix[h][nx][ny] = 1
                        tmp.append([h,nx,ny])
                    check[h][nx][ny] = True
            for i in range(2):
                nh = h + dh[i]
                if 0<= nh < H:
                    if matrix[nh][x][y] == 0 and check[nh][x][y] == False:
                        matrix[nh][x][y] = 1
                        tmp.append([nh,x,y])
                    check[nh][x][y] = True
        if tmp:
            cnt+=1
            queue.append(tmp)
    for row in check:
        for row2 in row:
            if False in row2:
                return -1
    return cnt
M,N,H = list(map(int,sys.stdin.readline().rstrip().split()))
matrix=[]
queue = []
result = 0
dx = [1,-1,0,0]
dy=[0,0,1,-1]
dh=[-1,1]
check = [[[False]*(M) for _ in range(N)] for _ in range(H)]
for h in range(H):
    matrix_tmp = []
    for i in range(N):
        tmp = list(map(int,sys.stdin.readline().rstrip().split()))
        matrix_tmp.append(tmp)
        for j in range(M):
            if tmp[j] == 1:
                queue.append([h,i,j])
            elif tmp[j] == -1:
                check[h][i][j] = True
    matrix.append(matrix_tmp)
queue = [queue]
print(bfs())
