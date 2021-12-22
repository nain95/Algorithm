import sys

def check(x: int, y : int, cur_matrix: list) -> None:
    ratio = 1
    while x + (1 * ratio) < n and 0 <= y + (-1  * ratio):
        cur_matrix[x + (1 * ratio)][y + (-1 * ratio)] = 0
        ratio += 1
    ratio = 1
    while x + (1 * ratio) < n and y + (1  * ratio) < n:
        cur_matrix[x + (1 * ratio)][y + (1 * ratio)] = 0
        ratio += 1

def dfs(x : int, y : int, matrix : list, ans : int, depth : int, cnt : int, flag : int) -> int:
    if ans > depth + cnt:
        return ans
    for i in range(x, n):
        tmp = 1
        if flag == 1:
            tmp = 0
        if i % 2 == 0:
            tmp = 0
            if flag == 1:
                tmp = 1
        for j in range(tmp, n, 2):
            if matrix[i][j] == 1:
                tmp_matrix = [item[:] for item in matrix]
                matrix[i][j] = 2
                check(i, j, matrix)
                ans = max(depth, dfs(i, j, matrix, ans, depth + 1, cnt - 1, flag))
                matrix = [item[:] for item in tmp_matrix]
    return ans

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    matrix = []
    white = 0
    black = 0
    for i in range(n):
        matrix.append(list(map(int, sys.stdin.readline().split())))
        for j in range(n):
            if i % 2 == 0:
                if j % 2 == 0:
                    if matrix[i][j] == 1:
                        white += 1
                else:
                    if matrix[i][j] == 1:
                        black += 1
            else:
                if j % 2 == 0:
                    if matrix[i][j] == 1:
                        black += 1
                else:
                    if matrix[i][j] == 1:
                        white += 1
    res = 0
    res += dfs(0, 0, matrix, 0 , 1, white, 0)
    res += dfs(0, 0, matrix, 0 , 1, black, 1)
    print(res)
