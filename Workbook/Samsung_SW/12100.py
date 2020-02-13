import sys
from _collections import deque
def left():
    global cube
    return_data = [[]*N for _ in range(N)]
    for i in range(len(cube)):
        temp = deque()
        check = 0
        for j in cube[i]:
            if j == 0:
                continue
            if len(temp) == 0:
                temp.append(j)
            elif temp[-1] == j and check == 0:
                temp[-1] *= 2
                check = 1
            else:
                temp.append(j)
                check = 0
        leng = len(temp)
        for z in range(leng):
            return_data[i].append(temp.popleft())
        for z in range(N-leng):
            return_data[i].append(0)
    cube = return_data.copy()
def right():
    global cube
    return_data = [[]*N for _ in range(N)]
    for i in range(len(cube)):
        temp = deque()
        check = 0
        for j in range(len(cube[i])-1,-1,-1):
            if cube[i][j] == 0:
                continue
            if len(temp) == 0:
                temp.append(cube[i][j])
                continue
            if temp[-1] == cube[i][j] and check == 0:
                temp[-1] *= 2
                check = 1
            else:
                temp.append(cube[i][j])
                check = 0
        leng = len(temp)
        for z in range(N-leng):
            return_data[i].append(0)
        for z in range(leng):
            return_data[i].append(temp.pop())
    cube = return_data.copy()
def up():
    global cube
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
                temp[-1] *= 2
                check = 1
            else:
                temp.append(cube[j][i])
                check = 0
        leng = len(temp)
        for z in range(leng):
            return_data[z][i] = temp.popleft()
    cube = return_data.copy()
def down():
    global cube
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
                temp[-1] *= 2
                check = 1
            else:
                temp.append(cube[j][i])
                check = 0
        leng = len(temp)
        for z in range(N-1,N-leng-1,-1):
            return_data[z][i] = temp.popleft()
    cube = return_data.copy()
def game(cur):
    global cube,max_num
    original = [x[:] for x in cube]
    max_data = 0
    if cur == 5:
        for i in cube:
            max_data = max(max_data,max(i))
        max_num = max(max_num,max_data)
        return
    for i in range(4):
        if i == 0:
            left()
            game(cur+1)
        elif i == 1:
            right()
            game(cur+1)
        elif i == 2:
            up()
            game(cur + 1)
        elif i == 3:
            down()
            game(cur + 1)
        cube = [x[:] for x in original]


N = int(sys.stdin.readline())
cube = []
for _ in range(N):
    cube.append(list(map(int, sys.stdin.readline().split())))
max_num = 0
game(0)
print(max_num)
