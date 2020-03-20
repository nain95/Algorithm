import sys
from _collections import deque


def bfs(start_node,end):
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    visit = []
    queue = deque()
    queue.append(start_node)
    length = 0
    chk = 0
    while queue:
        chk+=1
        sz = len(queue)
        for _ in range(sz):
            node = queue.popleft()
            if node not in visit:
                visit.append(node)
                if node == end:
                    return length
                for k in range(4):
                    nx,ny = node[0]+dx[k],node[1]+dy[k]
                    if 0<= nx < N and 0<= ny < N and 0 <= matrix[nx][ny] <= shark_size:
                        queue.append([nx,ny])
        length+=1
    if chk == 1:
        length = 0
    return length


def move(cur,fish_list):
    global shark,time,cnt
    fish_list = sorted(fish_list)
    min_len = 1000000
    min_index = 0
    for i in range(len(fish_list)):
        temp = bfs(cur, fish_list[i])
        if min_len > temp:
            min_len = temp
            min_index = i
    if min_len != 0:
        fish_list.pop(i)
        shark = fish_list[min_index]
        time += min_len
        cnt += 1
        matrix[shark[0]][shark[1]] = 0
        return True
    elif min_len == 0:
        return False

N = int(sys.stdin.readline())
fish = [[] for _ in range(7)]
matrix = []
shark_size = 2
time = 0
for i in range(N):
    matrix.append(list(map(int,sys.stdin.readline().split())))
    for j in range(N):
        if matrix[i][j] == 9:
            matrix[i][j] = 0
            shark = [i,j]
        elif 1 <= matrix[i][j] <= 6:
            fish[matrix[i][j]].append([i,j])
cnt = 0
fish_list = []
for i in range(1,shark_size):
    if i > 6:
        break
    for j in fish[i]:
        if matrix[j[0]][j[1]] != 0:
            fish_list.append(j)
while 1:
    if len(fish_list) == 1:
        fish_list.pop()
        time += bfs(shark, fish_list[0])
        shark = fish_list[0]
        cnt+=1
    elif move(shark,fish_list) == False:
        break
    if cnt == shark_size:
        shark_size += 1
        cnt = 0
        fish_list = []
        for i in range(1, shark_size):
            if i > 6:
                break
            for j in fish[i]:
                if matrix[j[0]][j[1]] != 0:
                    fish_list.append(j)
    if fish_list == []:
        break
print(time)