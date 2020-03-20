import sys,copy,itertools
from _collections import deque


def virus():
    queue = deque()
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    for i in range(N):
        for j in range(M):
            if data[i][j] == 2:
                queue.append([i,j])
    while queue:
        pop_data = queue.popleft()
        for z in range(4):
            nx,ny = pop_data[0]+dx[z],pop_data[1]+dy[z]
            if nx == -1 or ny == -1 or nx == N or ny == M:
                continue
            else:
                if data[nx][ny] == 0:
                    data[nx][ny] = 2
                    queue.append([nx,ny])

def solve(cur):
    global data,safe
    for tmp in itertool_list:
        original = copy.deepcopy(data)
        data[tmp[0][0]][tmp[0][1]] = 1
        data[tmp[1][0]][tmp[1][1]] = 1
        data[tmp[2][0]][tmp[2][1]] = 1
        virus()
        cnt = 0
        for i in data:
            cnt += i.count(0)
        safe = max(safe,cnt)
        data = copy.deepcopy(original)

N,M = map(int,sys.stdin.readline().split())
data = []
safe_list = deque()
for i in range(N):
    data.append(list(map(int,sys.stdin.readline().split())))
    for j in range(M):
        if data[i][j] == 0:
            safe_list.append([i,j])
itertool_list = list(itertools.combinations(safe_list,3))
safe = 0
solve(0)
print(safe)
