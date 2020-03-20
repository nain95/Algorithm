import sys
N = int(sys.stdin.readline().rstrip())
matrix = []
for _ in range(N):
    matrix.append(list(map(int,list(sys.stdin.readline().rstrip()))))
home_cnt = []
home_group = []
dx = [1,-1,0,0]
dy = [0,0,1,-1]
def bfs(cur,x,y):
    matrix[x][y] = 0

    queue = []
    queue.append([x,y])
    while len(queue) > 0:
        x,y = queue.pop()
        for k in range(0,4):
            nx,ny = x+dx[k],y+dy[k]
            if 0<=nx and nx<N and 0<=ny and ny<N:
                if matrix[nx][ny] == 1:
                    cur+=1
                    matrix[nx][ny]=0
                    queue.append([nx,ny])
    return cur
cnt =0
ans = []
for i in range(N):
    for j in range(N):
            if matrix[i][j] == 1 :
                ans.append(bfs(cnt+1,i,j))
print(len(ans))
for i in sorted(ans):
    print(i)