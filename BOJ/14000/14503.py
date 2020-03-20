import sys
n,m = map(int,sys.stdin.readline().split())
r,c,d = map(int,sys.stdin.readline().split())
map_data = []
for _ in range(n):
    map_data.append(list(map(int,sys.stdin.readline().split())))
cnt = 1
check = 0
dx = [-1,0,1,0]
dy = [0,1,0,-1]
while 1:
    map_data[r][c] = 2
    d = (d+3)%4
    if r+dx[d] < n and c+dy[d] < m:
        if map_data[r+dx[d]][c+dy[d]] == 0:
            r += dx[d]
            c += dy[d]
            cnt+=1
            check = 0
        else:
            check+=1
            if check == 4:
                if r + dx[(d+2)%4] < n and c + dy[(d+2)%4] < m:
                    if map_data[r+dx[(d+2)%4]][c+dy[(d+2)%4]] != 1:
                        r+=dx[d-2]
                        c+=dy[d-2]
                        check = 0
                    else:
                        print(cnt)
                        break