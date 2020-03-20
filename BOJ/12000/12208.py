import sys,copy,random
from _collections import deque
def left():
    return_data = [[0]*N for _ in range(N)]
    for i in range(N):
        temp = deque()
        check = 0
        for j in range(N):
            if cube[i][j] == 0:
                continue
            if len(temp) == 0:
                temp.append(cube[i][j])
            elif temp[-1] == cube[i][j] and check == 0:
                temp.append(temp.pop()*2)
                check = 1
            else:
                temp.append(cube[i][j])
                check = 0
        length = len(temp)
        for z in range(length):
            return_data[i][z] = temp.popleft()
    return return_data
def right():
    return_data = [[0]*N for _ in range(N)]
    for i in range(N):
        temp = deque()
        check = 0
        for j in range(N-1,-1,-1):
            if cube[i][j] == 0:
                continue
            if len(temp) == 0:
                temp.append(cube[i][j])
                continue
            if temp[-1] == cube[i][j] and check == 0:
                temp.append(temp.pop()*2)
                check = 1
            else:
                temp.append(cube[i][j])
                check = 0
        length = len(temp)
        for z in range(N-1,N-length-1,-1):
            return_data[i][z] = temp.popleft()

    return return_data
def up():
    return_data = [[0]*N for _ in range(N)]
    for i in range(N):
        temp = deque()
        check = 0
        for j in range(N):
            if cube[j][i] == 0:
                continue
            if len(temp) == 0:
                temp.append(cube[j][i])
            elif temp[-1] == cube[j][i] and check == 0:
                temp.append(temp.pop()*2)
                check = 1
            else:
                temp.append(cube[j][i])
                check = 0
        leng = len(temp)
        for z in range(leng):
            return_data[z][i] = temp.popleft()
    return return_data
def down():
    return_data = [[0] * N for _ in range(N)]
    for i in range(N):
        temp = deque()
        check = 0
        for j in range(N-1,-1,-1):
            if cube[j][i] == 0:
                continue
            if len(temp) == 0:
                temp.append(cube[j][i])
            elif temp[-1] == cube[j][i] and check == 0:
                temp.append(temp.pop() * 2)
                check = 1
            else:
                temp.append(cube[j][i])
                check = 0
        leng = len(temp)
        for z in range(N-1,N-leng-1,-1):
            return_data[z][i] = temp.popleft()
    return return_data
M = int(sys.stdin.readline())
for i in range(M):
    N,spin = sys.stdin.readline().split()
    N = int(N)
    cube = []
    for _ in range(N):
        cube.append(list(map(int,sys.stdin.readline().split())))

    if spin == 'right':
        res = right()
    elif spin == 'up':
        res = up()
    elif spin == 'down':
        res = down()
    else:
        res = left()
    print('Case #' + str(i + 1) + ':')
    for j in range(len(res)):
        for z in range(len(res[j])):
            if z == len(res[j]) - 1:
                print(res[j][z], end='')
            else:
                print(res[j][z], end=' ')
        print()