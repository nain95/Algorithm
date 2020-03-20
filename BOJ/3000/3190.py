import sys
from _collections import deque
N = int(sys.stdin.readline())
K = int(sys.stdin.readline())
matrix = [[0]*(N+2) for _ in range(N+2)]
matrix[0] = [-1]*(N+2)
matrix[-1] = [-1]*(N+2)
for i in range(N+2):
    matrix[i][0] = -1
    matrix[i][N+1] = -1
for _ in range(K):
    apple = list(map(int,sys.stdin.readline().split()))
    matrix[apple[0]][apple[1]] = 1
L = int(sys.stdin.readline())
L_data = deque()
for _ in range(L):
    temp = sys.stdin.readline().split()
    L_data.append([int(temp[0]),temp[1]])
time = 0
head = [1,1]
snake = deque()
cur_L = 'R'
spin_D = ['R','D','L','U']
spin_L = ['R','U','L','D']

while 1:
    time+=1
    snake.append([head[0], head[1]])
    if cur_L == 'R':
        head[1] += 1
    elif cur_L == 'D':
        head[0] += 1
    elif cur_L == 'L':
        head[1] -= 1
    else:
        head[0] -= 1
    if matrix[head[0]][head[1]] == -1 or head in snake:
        print(time)
        sys.exit()
    elif matrix[head[0]][head[1]] == 1:
        matrix[head[0]][head[1]] = 0
    else:
        snake.popleft()
    if L_data:
        if time == L_data[0][0]:
            popdata = L_data.popleft()
            if popdata[1] == 'D':
                cur_L = spin_D[(spin_D.index(cur_L)+1)%4]
            else:
                cur_L = spin_L[(spin_L.index(cur_L) + 1) % 4]


