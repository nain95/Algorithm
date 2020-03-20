import sys
from _collections import deque
R,C = map(int,sys.stdin.readline().split())
data = []
W = []
for i in range(R):
    data.append(list(sys.stdin.readline().rstrip()))
    if 'S' in data[i]:
        S = [i,data[i].index('S')]
    if 'D' in data[i]:
        D = [i,data[i].index('D')]
    if '*' in data[i]:
        W.append([i,data[i].index('*')])
queue = deque([S])
check = [[-1]*C for _ in range(R)]
check[S[0]][S[1]] = 0
dx = [1,-1,0,0]
dy = [0,0,1,-1]
cnt=0
chk = 0
while queue:
    cur = queue.popleft()
    if check[cur[0]][cur[1]] == chk:
        tmp = []
        for j in W:
            for i in range(4):
                jx, jy = j[0] + dx[i], j[1] + dy[i]
                if jx >= R or jy >= C or jx < 0 or jy < 0:
                    continue
                elif data[jx][jy] == '.':
                    tmp.append([jx, jy])
                    data[jx][jy] = '*'
                else:
                    continue
        W += tmp
        chk+=1
    for i in range(4):
        nx,ny = cur[0]+dx[i],cur[1]+dy[i]
        if nx >= R or ny >= C or nx < 0 or ny < 0:
            continue
        elif data[nx][ny] == '*' or data[nx][ny] == 'X':
            continue
        else:
            if check[nx][ny] == -1:
                check[nx][ny] = check[cur[0]][cur[1]]+1
                queue.append([nx,ny])
                if data[nx][ny] == 'D':
                    print(check[nx][ny])
                    sys.exit()
print('KAKTUS')