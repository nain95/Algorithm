import sys
from _collections import deque
def Right(M,Red,Blue):
    i = 1
    j = 1
    if Red[0] == Blue[0]:
        if Red[1] < Blue[1]:
            temp = 1
        else:
            temp = 0
        while 1:
            if M[Red[0]][Red[1]+i] == '#':
                Red = [Red[0],Red[1]+i-1]
                break
            elif M[Red[0]][Red[1]+i] == 'O':
                Red = [Red[0], Red[1] + i]
                break
            i+=1
        while 1:
            if M[Blue[0]][ Blue[1] + j] == '#':
                Blue = [Blue[0], Blue[1] + j - 1]
                break
            elif M[Blue[0]][ Blue[1] + j] == 'O':
                Blue = [Blue[0], Blue[1] + j]
                break
            j+=1
        if Red == Blue != Zero_index:
            if temp == 1:
                Red[1] -= 1
            else:
                Blue[1] -= 1
    else:
        while 1:
            if M[Red[0]][Red[1] + i] == '#':
                Red = [Red[0], Red[1] + i - 1]
                break
            elif  M[Red[0]][Red[1] + i] == 'O':
                Red = [Red[0], Red[1] + i]
                break
            i += 1
        while 1:
            if M[Blue[0]][Blue[1] + j] == '#':
                Blue = [Blue[0], Blue[1] + j - 1]
                break
            elif M[Blue[0]][Blue[1] + j] == 'O':
                Blue = [Blue[0], Blue[1] + j]
                break
            j += 1
    return Red+Blue
def Left(M,Red,Blue):
    i = 1
    j = 1
    if Red[0] == Blue[0]:
        if Red[1] < Blue[1]:
            temp = 1
        else:
            temp = 0
        while 1:
            if M[Red[0]][ Red[1] - i] == '#':
                Red = [Red[0], Red[1] - i + 1]
                break
            elif M[Red[0]][ Red[1] - i] == 'O':
                Red = [Red[0], Red[1] - i]
                break
            i+=1
        while 1:
            if M[Blue[0]][ Blue[1] - j] == '#':
                Blue = [Blue[0], Blue[1] - j + 1]
                break
            elif M[Blue[0]][ Blue[1] - j] == 'O':
                Blue = [Blue[0], Blue[1] - j]
                break
            j += 1
        if Red == Blue != Zero_index:
            if temp == 1:
                Blue[1] += 1
            else:
                Red[1] += 1
    else:
        while 1:
            if M[Red[0]][Red[1] - i] == '#':
                Red = [Red[0], Red[1] - i + 1]
                break
            elif M[Red[0]][Red[1] - i] == 'O':
                Red = [Red[0], Red[1] - i]
                break
            i+=1
        while 1:
            if M[Blue[0]][Blue[1] - j] == '#':
                Blue = [Blue[0], Blue[1] - j + 1]
                break
            elif M[Blue[0]][Blue[1] - j] == 'O':
                Blue = [Blue[0], Blue[1] - j]
                break
            j += 1
    return Red + Blue
def Top(M,Red,Blue):
    i = 1
    j = 1
    if Red[1] == Blue[1]:
        if Red[0] < Blue[0]:
            temp = 1
        else:
            temp = 0
        while 1:
            if M[Red[0] - i][ Red[1]] == '#':
                Red = [Red[0] - i + 1, Red[1]]
                break
            elif M[Red[0] - i][ Red[1]] == 'O':
                Red = [Red[0] - i, Red[1]]
                break
            i+=1
        while 1:
            if M[Blue[0] - j][ Blue[1]] == '#':
                Blue = [Blue[0] - j + 1, Blue[1]]
                break
            elif M[Blue[0] - j][ Blue[1]] == 'O':
                Blue = [Blue[0] - j, Blue[1]]
                break
            j += 1
        if Red == Blue != Zero_index:
            if temp == 1:
                Blue[0] += 1
            else:
                Red[0] += 1
    else:
        while 1:
            if M[Red[0] - i][ Red[1]] == '#':
                Red = [Red[0] - i + 1, Red[1]]
                break
            elif M[Red[0] - i][ Red[1]] == 'O':
                Red = [Red[0] - i, Red[1]]
                break
            i+=1
        while 1:
            if M[Blue[0] - j][Blue[1]] == '#':
                Blue = [Blue[0] - j + 1, Blue[1]]
                break
            elif M[Blue[0] - j][ Blue[1]] == 'O':
                Blue = [Blue[0] - j, Blue[1]]
                break
            j += 1
    return Red + Blue
def Bottom(M,Red,Blue):
    i = 1
    j = 1
    if Red[1] == Blue[1]:
        if Red[0] < Blue[0]:
            temp = 1
        else:
            temp = 0
        while 1:
            if M[Red[0] + i][ Red[1]] == '#':
                Red = [Red[0] + i - 1, Red[1]]
                break
            elif M[Red[0] + i][Red[1]] == 'O':
                Red = [Red[0] + i, Red[1]]
                break
            i+=1
        while 1:
            if M[Blue[0] + j][ Blue[1]] == '#':
                Blue = [Blue[0] + j - 1, Blue[1]]
                break
            elif M[Blue[0] + j][ Blue[1]] == 'O':
                Blue = [Blue[0] + j , Blue[1]]
                break
            j += 1
        if Red == Blue != Zero_index:
            if temp == 1:
                Red[0] -= 1
            else:
                Blue[0] -= 1
    else:
        while 1:
            if M[Red[0] + i][Red[1]] == '#':
                Red = [Red[0] + i - 1, Red[1]]
                break
            elif M[Red[0] + i][Red[1]] == 'O':
                Red = [Red[0] + i, Red[1]]
                break
            i += 1
        while 1:
            if M[Blue[0] + j][Blue[1]] == '#':
                Blue = [Blue[0] + j - 1, Blue[1]]
                break
            elif M[Blue[0] + j][ Blue[1]] == 'O':
                Blue = [Blue[0] + j , Blue[1]]
                break
            j += 1
    return Red + Blue
def marble_game(M,Red,Blue):
    Red+=Blue
    queue = deque([Red])
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    while queue:
        cur = queue.popleft()
        if cur[0:2] == Zero_index:
            if check[cur[0]][cur[1]][cur[2]][cur[3]] > 10:
                return -1
            return check[cur[0]][cur[1]][cur[2]][cur[3]]
        for i in range(4):
            nx,ny = cur[0]+dx[i],cur[1]+dy[i]
            bx,by = cur[2]+dx[i],cur[3]+dy[i]
            if M[bx][by] =='O':
                continue
            if M[nx][ny] !='#' or M[bx][by] !='#':
                if i == 0:
                    temp = Right(M,cur[:2],cur[2:])
                elif i == 1:
                    temp = Left(M,cur[:2],cur[2:])
                elif i == 2:
                    temp = Bottom(M,cur[:2],cur[2:])
                else:
                    temp = Top(M,cur[:2],cur[2:])
                if temp[2:] == Zero_index:
                    continue
                if check[temp[0]][temp[1]][temp[2]][temp[3]] == -1:
                    queue.append(temp)
                    check[temp[0]][temp[1]][temp[2]][temp[3]] = check[cur[0]][cur[1]][cur[2]][cur[3]]+1
                    if check[cur[0]][cur[1]][cur[2]][cur[3]] > 10:
                        return -1
    return -1

num = list(map(int,sys.stdin.readline().rstrip().split()))
matrix = []
for i in range(num[0]):
    matrix.append(list(sys.stdin.readline().rstrip()))
    if 'O' in matrix[i]:
        Zero_index = [i, matrix[i].index('O')]
    if 'R' in matrix[i]:
        R_index = [i,matrix[i].index('R')]
    if 'B' in matrix[i]:
        B_index = [i,matrix[i].index('B')]
check = [[[[-1]*num[1] for _ in range(num[0])] for _ in range(num[1])] for _ in range(num[0])]
check[R_index[0]][R_index[1]][B_index[0]][B_index[1]] = 0

print(marble_game(matrix,R_index,B_index))