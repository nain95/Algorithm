import sys
from _collections import deque
def left():
    global score
    return_data = [[0]*N for _ in range(N)]
    for i in range(N):
        temp = deque()
        check = 0
        for j in range(N):
            if cube[i][j] == 0:
                check = 0
                continue
            if len(temp) == 0:
                temp.append(cube[i][j])
            elif temp[-1] == cube[i][j] and check == 0:
                temp.append(temp.pop()*2)
                score+=temp[-1]
                check = 1
            else:
                temp.append(cube[i][j])
                check = 0
        length = len(temp)
        for z in range(length):
            return_data[i][z] = temp.popleft()
    return return_data
def right():
    global score
    return_data = [[0]*N for _ in range(N)]
    for i in range(N):
        temp = deque()
        check = 0
        for j in range(N-1,-1,-1):
            if cube[i][j] == 0:
                check = 0
                continue
            if len(temp) == 0:
                temp.append(cube[i][j])
                continue
            if temp[-1] == cube[i][j] and check == 0:
                temp.append(temp.pop()*2)
                score += temp[-1]
                check = 1
            else:
                temp.append(cube[i][j])
                check = 0
        length = len(temp)
        for z in range(N-1,N-length-1,-1):
            return_data[i][z] = temp.popleft()

    return return_data
def up():
    global score
    return_data = [[0]*N for _ in range(N)]
    for i in range(N):
        temp = deque()
        check = 0
        for j in range(N):
            if cube[j][i] == 0:
                check = 0
                continue
            if len(temp) == 0:
                temp.append(cube[j][i])
            elif temp[-1] == cube[j][i] and check == 0:
                temp.append(temp.pop()*2)
                score += temp[-1]
                check = 1
            else:
                temp.append(cube[j][i])
                check = 0
        leng = len(temp)
        for z in range(leng):
            return_data[z][i] = temp.popleft()
    return return_data
def down():
    global score
    return_data = [[0] * N for _ in range(N)]
    for i in range(N):
        temp = deque()
        check = 0
        for j in range(N-1,-1,-1):
            if cube[j][i] == 0:
                check = 0
                continue
            if len(temp) == 0:
                temp.append(cube[j][i])
            elif temp[-1] == cube[j][i] and check == 0:
                temp.append(temp.pop() * 2)
                score += temp[-1]
                check = 1
            else:
                temp.append(cube[j][i])
                check = 0
        leng = len(temp)
        for z in range(N-1,N-leng-1,-1):
            return_data[z][i] = temp.popleft()
    return return_data
score = int(sys.stdin.readline())
case = sys.stdin.readline().rstrip()
case_list = deque()
cube_list = list(map(int,sys.stdin.readline().split()))
cube = []
N = 4
for i in range(0,len(case),4):
    case_list.append(case[i:i+4])
    if i+3 < len(cube_list):
        cube.append(cube_list[i:i+4])
while case_list:
    pop_data = case_list.popleft()
    if pop_data[0] == 'L':
        cube = left()
    elif pop_data[0] == 'R':
        cube = right()
    elif pop_data[0] == 'U':
        cube = up()
    elif pop_data[0] == 'D':
        cube = down()
    cube[int(pop_data[2])][int(pop_data[3])] = int(pop_data[1])
print(score)