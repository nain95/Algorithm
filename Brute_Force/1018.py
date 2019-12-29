import sys
def check(C):
    num1 = 0
    num2 = 0
    for i in range(8):
        for j in range(8):
            if i%2 == 0 and j%2 == 0:
                if C[i][j] == 'B':
                    num1+=1
            elif i%2 ==0 and j%2 != 0:
                if C[i][j] == 'W':
                    num1+=1
            elif i%2 != 0 and j%2 ==0:
                if C[i][j] == 'W':
                    num1+=1
            else:
                if C[i][j] =='B':
                    num1+=1
        for j in range(8):
            if i % 2 == 0 and j % 2 == 0:
                if C[i][j] == 'W':
                    num2 += 1
            elif i % 2 == 0 and j % 2 != 0:
                if C[i][j] == 'B':
                    num2 += 1
            elif i % 2 != 0 and j % 2 == 0:
                if C[i][j] == 'B':
                    num2 += 1
            else:
                if C[i][j] == 'W':
                    num2 += 1
    return min(num1,num2)
def create_matrix(M):
    result = []
    i = 0
    j = 0
    y = 0
    for z in range((len(M)-7)*(len(M[0])-7)):
        temp_matrix = []
        for i in range(y,y+8):
                temp_matrix.append(M[i][j:j+8])
        result.append(check(temp_matrix))
        if y+8 < len(M):
            y+=1
            continue
        elif j+8<len(M[0]):
            y=0
            j+=1
            continue
        else:
            break
    print(min(result))


num_list = list(map(int,(sys.stdin.readline().rstrip().split())))
matrix = []
for i in range(num_list[0]):
    temp = list((sys.stdin.readline().rstrip()))
    matrix.append(temp)
create_matrix(matrix)