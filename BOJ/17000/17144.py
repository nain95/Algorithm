import sys,copy
from _collections import deque


def fine_dust():
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    tmp_map = copy.deepcopy(data)
    for i in range(r):
        for j in range(c):
            if data[i][j] != -1 and data[i][j] != 0:
                spread = data[i][j] // 5
                for k in range(4):
                    nx,ny = i+dx[k], j+dy[k]
                    if 0 <= nx < r and 0 <= ny < c:
                        if data[nx][ny] != -1:
                            tmp_map[i][j] -= spread
                            tmp_map[nx][ny] += spread
    return tmp_map

def clean():
    data[air_cleaner[0]-1][0] = 0
    data[air_cleaner[1]+1][0] = 0

    for i in range(air_cleaner[0]-1,0,-1):
        data[i][0] = data[i - 1][0]
    for i in range(air_cleaner[1]+1,r-1):
        data[i][0] = data[i + 1][0]
    for j in range(c-1):
        data[0][j] = data[0][j+1]
        data[r-1][j] = data[r-1][j+1]
    for i in range(air_cleaner[0]):
        data[i][c-1] = data[i+1][c-1]
    for i in range(r-1,air_cleaner[1] - 1,-1):
        data[i][c - 1] = data[i - 1][c - 1]
    for j in range(c-1,1,-1):
        data[air_cleaner[0]][j] = data[air_cleaner[0]][j-1]
        data[air_cleaner[1]][j] = data[air_cleaner[1]][j-1]
    data[air_cleaner[0]][1] = 0
    data[air_cleaner[1]][1] = 0
r,c,t = map(int,sys.stdin.readline().split())
data = []
air_cleaner = []
queue = deque()
for i in range(r):
    data.append(list(map(int,sys.stdin.readline().split())))
    if data[i][0] == -1:
        air_cleaner.append(i)
for _ in range(t):
    data = copy.deepcopy(fine_dust())
    clean()
result = 2
for d in data:
    result += sum(d)
print(result)
