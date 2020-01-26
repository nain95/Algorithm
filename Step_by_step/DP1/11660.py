import sys,copy
N,M = map(int,sys.stdin.readline().split())
data = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
sum_matrix = copy.deepcopy(data)
for i in range(N):
    for j in range(N):
        if i == 0 and j == 0:
            pass
        elif i == 0:
            sum_matrix[0][j] += sum_matrix[0][j-1]
        elif j == 0:
            sum_matrix[i][0] += sum_matrix[i-1][0]
        else:
            sum_matrix[i][j] += sum_matrix[i-1][j] + sum(data[i][:j])
for _ in range(M):
    x1,y1,x2,y2 = map(int,sys.stdin.readline().split())

    if x1 == 1 and y1 == 1:
        print(sum_matrix[x2 - 1][y2 - 1])
    elif x1 == 1:
        print(sum_matrix[x2 - 1][y2 - 1] - sum_matrix[x2 - 1][y1 - 2])
    elif y1 == 1:
        print(sum_matrix[x2 - 1][y2 - 1] - sum_matrix[x1 - 2][y2 - 1])
    else:
        print(sum_matrix[x2 - 1][y2 - 1] - sum_matrix[x1 - 2][y2 - 1] - sum_matrix[x2 - 1][y1 - 2] + sum_matrix[x1 - 2][y1 - 2])