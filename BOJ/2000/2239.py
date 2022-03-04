import sys
S_data = []
zero_data = []
for i in range(9):
    temp_data = list(map(int,list(sys.stdin.readline().rstrip())))
    if 0 in temp_data:
        temp = temp_data.index(0)
    for j in range(9):
        if temp_data[j] == 0:
            zero_data.append([i,j])
    S_data.append(temp_data)

def check(x,y,num):
    if num in S_data[x]:
        return True
    for z in range(9):
        if S_data[z][y] == num:
            return True
    temp_x = x//3*3
    temp_y = y//3*3
    for i in range(temp_x,temp_x+3):
        for j in range(temp_y,temp_y+3):
            if S_data[i][j] == num:
                return True
    return False

def sudoku(cur):
    if cur == len(zero_data):
        for i in range(9):
            for j in range(9):
                print(S_data[i][j],end='')
            print()
        sys.exit()
    for z in range(1,10):
        if check(zero_data[cur][0],zero_data[cur][1],z):
            continue
        S_data[zero_data[cur][0]][zero_data[cur][1]]=z
        sudoku(cur+1)
        S_data[zero_data[cur][0]][zero_data[cur][1]]=0

sudoku(0)