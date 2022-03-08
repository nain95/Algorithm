import sys
from collections import deque, defaultdict

aaa = []
t = int(sys.stdin.readline())
for _ in range(t):
    h, w = map(int, sys.stdin.readline().split())
    matrix = [list(sys.stdin.readline().rstrip()) for _ in range(h)]
    queue = deque()
    key_dic = defaultdict(int)
    door_dic = defaultdict(list)
    ans = 0
    for key in list(sys.stdin.readline().rstrip()):
        key_dic[key] = 1
    for i in range(h):
        if i == 0 or i == h - 1:
            for j in range(w):
                if matrix[i][j] != '*':
                    if matrix[i][j].isupper():
                        door_dic[matrix[i][j]].append((i, j))
                    else:
                        queue.append((i, j)) 
        else:
            if matrix[i][0] != '*':
                if matrix[i][0].isupper():
                    door_dic[matrix[i][0]].append((i, 0))
                else:
                    queue.append((i, 0))
            if matrix[i][w-1] != '*':
                if matrix[i][w-1].isupper():
                    door_dic[matrix[i][w-1]].append((i, w-1))
                else:
                    queue.append((i, w-1))
    dx, dy = (0, 0, 1, -1), (1, -1, 0, 0)
    visited = [[0] * w for _ in range(h)]
    for key in key_dic.keys():
        if key.upper() in door_dic:
            for res in door_dic[key.upper()]:
                queue.append(res)
    while queue:
        x, y = queue.popleft()
        if visited[x][y] == 1:
            continue
        elif matrix[x][y] == '$':
            ans += 1
        elif matrix[x][y].islower():
            if door_dic[matrix[x][y].upper()]:
                for res in door_dic[matrix[x][y].upper()]:
                    queue.append(res)
            key_dic[matrix[x][y]] = 1
        visited[x][y] = 1
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < h and 0 <= ny < w and visited[nx][ny] == 0:
                value = matrix[nx][ny]
                if value == '.' or value =='$':
                    queue.append((nx, ny))
                elif value.isalpha():
                    if value.isupper():
                        if value.lower() in key_dic:
                            queue.append((nx, ny))
                        else:
                            door_dic[value].append((nx, ny))
                    else:
                        if value.upper() in door_dic:
                            for res in door_dic[value.upper()]:
                                queue.append(res)
                        key_dic[value] = 1
                        queue.append((nx, ny))
    print(ans)