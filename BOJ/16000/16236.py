import sys
from _collections import deque


def bfs():
    global shark
    dx = [-1,0,1,0]
    dy = [0,-1,0,1]
    visit = [[0]*N for _ in range(N)]
    queue = deque([shark])
    cnt = 0
    while queue:
        cnt += 1
        sz = len(queue)
        eat_list = []
        for _ in range(sz):
            node = queue.popleft()
            x,y = node[0], node[1]
            if not visit[x][y]:
                visit[x][y] = 1
                for k in range(4):
                    nx,ny = x+dx[k],y+dy[k]
                    if 0 <= nx < N and 0 <= ny < N and 0 <= matrix[nx][ny] <= shark_size and not visit[nx][ny]:
                        if 0 < matrix[nx][ny] < shark_size:
                            eat_list.append([nx,ny])
                        queue.append([nx,ny])
        if eat_list:
            eat_list = sorted(eat_list)
            matrix[eat_list[0][0]][eat_list[0][1]] = 0
            shark = [eat_list[0][0],eat_list[0][1]]
            return cnt

    return -1


N = int(sys.stdin.readline())
# fish = [[] for _ in range(7)]
matrix = []
shark_size = 2
time = 0
matrix=[[int(x)for x in sys.stdin.readline().split()] for y in range(N)]
for i in range(N):
    # matrix.append(list(map(int,sys.stdin.readline().split())))
    for j in range(N):
        if matrix[i][j] == 9:
            matrix[i][j] = 0
            shark = [i,j]
            break
cnt = 0
while 1:
    tmp = bfs()
    if tmp != -1:
        time += tmp
        cnt += 1
    else:
        break
    if cnt == shark_size:
        shark_size += 1
        cnt = 0
print(time)