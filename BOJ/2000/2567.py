import sys

num = int(sys.stdin.readline())
position = []
for _ in range(num):
    position.append(list(map(int, sys.stdin.readline().split())))

answer = 0
cube = [[0 for _ in range(102)] for _ in range(102)]
for pos in position:
    for i in range(0,10):
        for j in range(0,10):
            cube[pos[0]+i][pos[1]+j] = 1
dx = [1,0,0,-1]
dy = [0,1,-1,0]
for i in range(102):
    for j in range(102):
        if cube[i][j] == 1:
            for k in range(4):
                if cube[i+dx[k]][j+dy[k]] == 0:
                    answer += 1
print(answer)