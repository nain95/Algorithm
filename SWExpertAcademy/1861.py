import sys
from _collections import deque

def bfs(index,num):
    queue = deque([index])
    result = 0
    while queue:
        length = len(queue)
        result += 1
        dx = [1,-1,0,0]
        dy = [0,0,-1,1]
        for _ in range(length):
            x, y = queue.popleft()
            for k in range(4):
                nx, ny = x + dx[k], y + dy[k]
                if 0 <= nx < n and 0 <= ny < n:
                    if room[x][y]+1 == room[nx][ny]:
                        queue.append([nx,ny])
    return result

t = int(sys.stdin.readline())
for case in range(t):
    max_value = 0
    max_index = 0
    n = int(sys.stdin.readline())
    room = []
    for _ in range(n):
        room.append(list(map(int,sys.stdin.readline().split())))
    for x in range(n):
        for y in range(n):
            value = bfs([x,y],room[x][y])
            if max_value < value:
                max_value = value
                max_num = room[x][y]
            elif max_value == value:
                max_num = min(max_num,room[x][y])
    print(f'#{case+1} {max_num} {max_value}')