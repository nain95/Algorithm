import sys

r, c, m = map(int, sys.stdin.readline().split())
shark = [[[] for _ in range(c)] for _ in range(r)]
for _ in range(m):
    x, y, s, d, z = map(int, sys.stdin.readline().split())
    shark[x-1][y-1] = [z, s, d]
time = 0
shark_cnt = 0
ans = 0
length = ((r-1) * 2, (c-1) * 2)
dx, dy = (0, -1, 1, 0, 0), (0, 0, 0, 1, -1)
while time < c and shark_cnt != m:
    for i in range(r):
        if shark[i][time]:
            ans += shark[i][time][0]
            shark[i][time] = []
            break
    move = []
    for x in range(r):
        for y in range(c):
            if shark[x][y]:
                if shark[x][y][2] == 1 or shark[x][y][2] == 2:
                    speed = shark[x][y][1] % length[0]
                    nx = x
                    for _ in range(speed):
                        if nx == 0 and shark[x][y][2] == 1:
                            shark[x][y][2] = 2
                        elif nx == r-1 and shark[x][y][2] == 2:
                            shark[x][y][2] = 1
                        nx += dx[shark[x][y][2]]
                    move.append([nx,y] + shark[x][y][:])
                elif shark[x][y][2] == 3 or shark[x][y][2] == 4:
                    speed = shark[x][y][1] % length[1]
                    ny = y
                    for _ in range(speed):
                        if ny == c-1 and shark[x][y][2] == 3:
                            shark[x][y][2] = 4
                        elif ny == 0 and shark[x][y][2] == 4:
                            shark[x][y][2] = 3
                        ny += dy[shark[x][y][2]]
                    move.append([x,ny] + shark[x][y][:])
    shark = [[[] for _ in range(c)] for _ in range(r)]
    for i, j, z, s, d in move:
        if shark[i][j]:
            shark[i][j] = max(shark[i][j],[z, s, d])
        else:
            shark[i][j] = [z, s, d]
    time += 1
print(ans)