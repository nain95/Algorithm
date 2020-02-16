import sys
N,M,X,Y,K = map(int,sys.stdin.readline().split())
map_data = []
dice = [[0,0,0,0],[0,0]]
for i in range(N):
    map_data.append(list(map(int,sys.stdin.readline().split())))
K_list = list(map(int,sys.stdin.readline().split()))
def left():
    temp = dice[1][0]
    dice[1][0] = dice[0][1]
    dice[0][1] = dice[1][1]
    dice[1][1] = dice[0][3]
    dice[0][3] = temp
def right():
    temp = dice[1][0]
    dice[1][0] = dice[0][3]
    dice[0][3] = dice[1][1]
    dice[1][1] = dice[0][1]
    dice[0][1] = temp
def down():
    temp = dice[0][0]
    dice[0][0] = dice[0][1]
    dice[0][1] = dice[0][2]
    dice[0][2] = dice[0][3]
    dice[0][3] = temp
def up():
    temp = dice[0][3]
    dice[0][3] = dice[0][2]
    dice[0][2] = dice[0][1]
    dice[0][1] = dice[0][0]
    dice[0][0] = temp

for i in K_list:
    if i == 1:
        if Y+1 == M:
            continue
        Y+=1
        right()
    elif i == 2:
        if Y == 0:
            continue
        Y-=1
        left()
    elif i == 3:
        if X == 0:
            continue
        X-=1
        up()
    else:
        if X+1 == N:
            continue
        X+=1
        down()
    if map_data[X][Y] == 0:
        map_data[X][Y] = dice[0][1]
    else:
        dice[0][1] = map_data[X][Y]
        map_data[X][Y] = 0
    print(dice[0][3])