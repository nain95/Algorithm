import sys

def dfs(x, y, n, visited, board, type):
    res = 0
    depth = 1
    dx, dy = (-1, -1, 0, 1, 1), (0, 1, 1, 1, 0)
    stack = [(x, y, -1, 1)]
    while stack:
        # print(stack)
        x, y, direction, depth = stack.pop()
        if depth == n:
            nx, ny = x + dx[direction], y + dy[direction]
            if (0 <= nx < len(board) and 0 <= ny < len(board[0]) and board[nx][ny] != type) or (nx < 0 or nx >= len(board) or ny < 0 or ny >= len(board[0])):
                return 1
        if direction == -1:
            for k in range(5):
                if visited[x][y][k] == 1:
                    continue
                nx, ny = x + dx[k], y + dy[k]
                if 0 <= nx < len(board) and 0 <= ny < len(board[0]) and visited[nx][ny][k] == -1 and  board[nx][ny] == type:
                    stack.append((nx, ny, k, depth + 1))
                    visited[nx][ny][k] = 1
                    # visited[nx][ny][(k + 4) % 5] = 1
        else:
            nx, ny = x + dx[direction], y + dy[direction]
            if 0 <= nx < len(board) and 0 <= ny < len(board[0]) and visited[nx][ny][direction] == -1 and  board[nx][ny] == type:
                stack.append((nx, ny, direction, depth + 1))
                visited[nx][ny][direction] = 1
                # visited[nx][ny][(direction + 4) % 5] = 1
    return 0

def solution(h, w, n, board):
    visited = [[[-1] * 5 for _ in range(w)] for _ in range(h)]
    for j in range(h):
        for i in range(w):
            if board[i][j] != 0:
                if dfs(i, j, n, visited, board, board[i][j]):
                    return (i, j, board[i][j])
    return (-1, -1, -1)

if __name__ == '__main__':
    board = [list(map(int, sys.stdin.readline().split())) for _ in range(19)]
    x, y, type = solution(19, 19, 5, board)
    if type == -1:
        print(0)
    else:
        print(type)
        print(x + 1, y + 1)