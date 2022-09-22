import sys
from collections import deque

def find(parents, x):
    # if parents[x] != x:
    if parents[x] >= 0:
        y = find(parents, parents[x])
        parents[x] = y
        return y
        # return find(parents, parents[x])
    return x

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a == b:
        return
    # if a < b:
    #     parent[b] = a
    #     # parent[a] = a
    # else:
    #     parent[a] = b
    #     # parent[b] = b
    if parents[a] < parents[b]:
        parents[a] += parents[b]
        parents[b] = a
    else:
        parents[b] += parents[a]
        parents[a] = b



def convert(x, y):
    return x * c + y

def bfs(visited, start):
    queue = deque([start])
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
    s = convert(start[0], start[1])
    melt_list = []
    while queue:
        x, y = queue.popleft()
        visited[x][y] = 1
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < r and 0 <= ny < c:
                if visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    # union(parents, convert(x, y), convert(nx, ny))
                    parents[convert(nx,ny)] = parents[s]
                    if matrix[nx][ny] == '.':
                        queue.append([nx, ny])
                    elif matrix[nx][ny] == 'X':
                        melt_list.append([nx, ny])
                elif matrix[nx][ny] == '.':
                    union(parents, convert(x, y), convert(nx, ny))
                    # parents[convert(nx,ny)] = parents[convert(x, y)]
    return melt_list

r, c = map(int, sys.stdin.readline().split())
matrix = []
answer = -1
# parents = [i for i in range(r * c)]
parents = [-1 for i in range(r * c)]
swan = []
for i in range(r):
    matrix.append(list(sys.stdin.readline().rstrip()))
    for j, cmd in enumerate(matrix[i]):
        if cmd == 'L':
            swan.append(convert(i, j))
            matrix[i][j] = '.'
visited = [[0] * c for _ in range(r)]
if find(parents, swan[0]) != find(parents, swan[1]):
    answer += 1
    melt = []
    for x in range(r):
        for y in range(c):
            if matrix[x][y] == '.' and visited[x][y] == 0:
                melt += bfs(visited, [x, y])
    for i, j in melt:
        visited[i][j] = 0
        matrix[i][j] = '.'
    while find(parents, swan[0]) != find(parents, swan[1]):
        answer += 1
        copy_melt = melt[:]
        melt = []
        for x, y in copy_melt:
            if matrix[x][y] == '.' and visited[x][y] == 0:
                melt += bfs(visited, [x, y])
        for i, j in melt:
            visited[i][j] = 0
            matrix[i][j] = '.'
print(answer)

