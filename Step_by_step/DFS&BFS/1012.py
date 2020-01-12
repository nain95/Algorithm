import sys
dx=[1,-1,0,0]
dy=[0,0,1,-1]
def bfs(x,y):
    matrix[x][y] = 0
    queue=[]
    queue.append([x,y])
    while queue != []:
        x,y = queue.pop()
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if nx>=0 and nx < N and ny>=0 and ny < M:
                if matrix[nx][ny] == 1:
                    queue.append([nx,ny])
                    matrix[nx][ny] = 0

T = int(input())
for _ in range(T):
    cnt = 0
    M, N, K = list(map(int,sys.stdin.readline().rstrip().split()))
    matrix = [[0]*M for _ in range(N)]
    for _ in range(K):
        tmp = list(map(int,sys.stdin.readline().rstrip().split()))
        matrix[tmp[1]][tmp[0]] = 1
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 1:
                bfs(i,j)
                cnt+=1
    print(cnt)