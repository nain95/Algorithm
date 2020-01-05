import sys
def print_matrix(M):
    print('---------------')
    for i in M:
        for j in i:
            print(j,end='')
        print()
    print('---------------')

def Right(M,Red,Blue,Zero):
    while(1):
        i=1
        if M[Red[0],Red[1]+i] == '#':
            Red = [Red[0],Red[1]+i-1]
        if M[Blue[0],Blue[1]+i] == '#':

            i+=1
def Left(M,Red,Blue,Zero):
    while(1):
        i=1
        if M[Red[0],Red[1]-i] == '#':
            Red = [Red[0],Red[1]-i-1]
        i+=1
def Top(M,Red,Blue,Zero):
    while(1):
        i=1
        if M[Red[0]+i,Red[1]] == '#':
            Red = [Red[0]+i-1,Red[1]]
        i+=1
def Bottom(M,Red,Blue,Zero):
    while(1):
        i=1
        if M[Red[0]-i,Red[1]] == '#':
            Red = [Red[0]-i-1,Red[1]]
        i+=1
def marble_game(M,Red,Blue,Zero):
    print_matrix(M)
    stack=[]        #기울기가 가능한 경우
    if M[Red[0]-1][Red[1]]=='.':
        stack.append('T')
    if M[Red[0]+1][Red[1]]=='.':
        stack.append('B')
    if M[Red[0]][Red[1]-1]=='.':
        stack.append('L')
    if M[Red[0]][Red[1]+1]=='.':
        stack.append('R')
    print(stack)


num = list(map(int,sys.stdin.readline().rstrip().split()))
matrix = []
for i in range(num[0]):
    matrix.append(list(sys.stdin.readline().rstrip()))
    if '0' in matrix[i]:
        Zero_index = [i, matrix[i].index('0')]
    if 'R' in matrix[i]:
        R_index = [i,matrix[i].index('R')]
    if 'B' in matrix[i]:
        B_index = [i,matrix[i].index('B')]
marble_game(matrix,R_index,B_index,Zero_index)
