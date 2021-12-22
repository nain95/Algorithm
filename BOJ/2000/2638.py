import sys
from collections import defaultdict


def find_interior_space(matrix : list):
    visited = [[0] * m for _ in range(n)]
    stack = [[0, 0]]
    dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
    visited[0][0] = 1
    while stack:
        x, y = stack.pop()
        matrix[x][y] = 2
        for k in range(4):
            nx, ny = dx[k] + x, dy[k] + y
            if 0 <= nx < n and 0 <= ny < m and matrix[nx][ny] == 0 and visited[nx][ny] == 0:
                stack.append([nx, ny])
                visited[nx][ny] = 1

def find_melted_cheese(x: int, y: int) -> bool:
    dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
    air_cnt = 0
    for k in range(4):
        nx, ny = dx[k] + x, dy[k] + y
        if 0 <= nx < n and 0 <= ny < m and matrix[nx][ny] == 2:
            air_cnt += 1
            if air_cnt >= 2:
                return True
    return False

def find_cheese(matrix : list):
    melted = []
    visited = [[0] * m for _ in range(n)]
    dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
    copy_matrix = [item[:] for item in matrix]
    find_interior_space(matrix)
    while 1:
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 1 and visited[i][j] == 0:
                    stack = [[i,j]]
        if not stack:
            break
        visited[stack[0][0]][stack[0][1]] = 1
        while stack:
            x, y = stack.pop()
            if find_melted_cheese(x, y):
                melted.append([x, y])
            for k in range(4):
                nx, ny = dx[k] + x, dy[k] + y
                if 0 <= nx < n and 0 <= ny < m and matrix[nx][ny] == 1 and visited[nx][ny] == 0:
                    stack.append([nx, ny])
                    visited[nx][ny] = 1
    matrix = [item[:] for item in copy_matrix]
    for melted_x, melted_y in melted:
        matrix[melted_x][melted_y] = 0
    return matrix

def check_cheese(matrix: list) -> bool:
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 1:
                return True
    return False

if __name__ == "__main__":
    ans = 0
    n, m = map(int, sys.stdin.readline().split())
    matrix = []
    for _ in range(n):
        matrix.append(list(map(int, sys.stdin.readline().split())))
    while check_cheese(matrix):
        matrix = find_cheese(matrix)
        ans += 1
    print(ans)

