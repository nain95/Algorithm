import sys

def dfs(x, y, check):
    queue = [(x, y)]
    dx, dy = (0, 0, 1, -1), (1, -1, 0, 0)
    visited[x][y] = 1
    res = 0
    while queue:
        cur_x, cur_y = queue.pop()
        res += 1
        check_map[cur_x][cur_y] = check
        for k in range(4):
            nx, ny = cur_x + dx[k], cur_y + dy[k]
            if 0 <= nx < n and 0 <= ny < m and matrix[nx][ny] == 0 and visited[nx][ny] == 0:
                queue.append((nx, ny))
                visited[nx][ny] = 1
    dic[check] = res
    # return res


n, m = map(int, sys.stdin.readline().split())
ans = [[0] * m for _ in range(n)]
matrix = []
dic = {}
for _ in range(n):
    matrix.append(list(map(int, list(sys.stdin.readline().rstrip()))))
check = 0
check_map = [[-1] * m for _ in range(n)]
visited = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 0 and visited[i][j] == 0:
            dfs(i, j, check)
            check += 1
dx, dy = (0, 0, 1, -1), (1, -1, 0, 0)
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 1:
            tmp = set()
            for k in range(4):
                nx, ny = i + dx[k], j + dy[k]
                if 0 <= nx < n and 0 <= ny < m and matrix[nx][ny] == 0:
                    tmp.add(check_map[nx][ny])
            ans[i][j] += (sum([dic[t] for t in tmp]) + 1) % 10
for a in ans:
    for tmp in a:
        print(tmp, end='')
    print()