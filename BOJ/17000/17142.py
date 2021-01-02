import sys,copy,itertools
from _collections import deque


def spread():
    spread_time = 0
    tmp = 0
    queue = deque()
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    for i in range(N):
        for j in range(N):
            if data[i][j] == -1:
                queue.append([i,j])
    while queue:
        cnt = 0
        if tmp == ck:
            return (spread_time)
        spread_time += 1
        for _ in range(len(queue)):
            pop_data = queue.popleft()
            for z in range(4):
                nx, ny = pop_data[0]+dx[z],pop_data[1]+dy[z]
                if nx == -1 or ny == -1 or nx == N or ny == N:
                    continue
                else:
                    if data[nx][ny] == 0:
                        data[nx][ny] = -1
                        queue.append([nx,ny])
                        tmp += 1
                    elif data[nx][ny] == 2:
                        data[nx][ny] = -1
                        queue.append([nx, ny])
    return (spread_time)

def solve(cur):
    global data, safe, time, check
    for tmp in itertool_list:
        original = copy.deepcopy(data)
        for t in tmp:
            data[t[0]][t[1]] = -1
        virus_time = spread()
        cnt = 0
        for i in data:
            cnt += i.count(0)
        if cnt == 0:
            check = 1
            time = min(time, virus_time)
        data = copy.deepcopy(original)

N,M = map(int,(sys.stdin.readline().split()))
data = []
virus = deque()
ck = 0
for i in range(N):
    data.append(list(map(int,sys.stdin.readline().split())))
    for j in range(N):
        if data[i][j] == 2:
            virus.append([i,j])
        elif data[i][j] == 0:
            ck += 1
itertool_list = list(itertools.combinations(virus,M))
time = sys.maxsize
check = 0
solve(0)
if check == 0:
    print(-1)
else:
    print(time)

