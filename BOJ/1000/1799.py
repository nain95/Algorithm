import sys

def check(x: int, y : int, cur_matrix: list) -> int:
    ratio = 1
    while 0 <= x + (-1 * ratio) and 0 <= y + (-1  * ratio):
        if cur_matrix[x + (-1 * ratio)][y + (-1 * ratio)] == 2:
            return -1
        ratio += 1
    ratio = 1
    while 0 <= x + (-1 * ratio) and y + (1  * ratio) < n:
        if cur_matrix[x + (-1 * ratio)][y + (1 * ratio)] == 2:
            return -1
        ratio += 1
    return 1

def dfs(x : int, y : int, matrix : list, ans : int, depth : int, cnt : int) -> int:
    if ans > depth + cnt:
        return ans
    for i in range(x, n):
        tmp = 1
        if i % 2 == 0:
            tmp = 0
        for j in range(tmp, n, 2):
            if matrix[i][j] == 1 and check(i, j, matrix) == 1:
                tmp_matrix = matrix[:]
                tmp_matrix[i][j] = 2
                ans = max(depth, dfs(i, j, tmp_matrix, ans, depth + 1, cnt - 1))
                ans = max(depth, dfs(i, j, matrix[:], ans, depth, cnt))
                tmp_matrix[i][j] = 1
                matrix = tmp_matrix[:]
    return ans

def dfs2(x : int, y : int, matrix : list, ans : int, depth : int, cnt : int) -> int:
    if ans > depth + cnt:
        return ans
    for i in range(x, n):
        tmp = 0
        if i % 2 == 0:
            tmp = 1
        for j in range(tmp, n, 2):
            if matrix[i][j] == 1 and check(i, j, matrix) == 1:
                tmp_matrix = matrix[:]
                tmp_matrix[i][j] = 2
                ans = max(depth, dfs2(i, j, tmp_matrix, ans, depth + 1, cnt - 1))
                ans = max(depth, dfs2(i, j, matrix[:], ans, depth, cnt))
                tmp_matrix[i][j] = 1
                matrix = tmp_matrix[:]
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
    res += dfs(0, 0, matrix, 0 , 1, white)
    res += dfs2(0, 0, matrix, 0 , 1, black)
    print(res)
    #for i in range(n):
    #    for j in range(n):
    #        if matrix[i][j] == 1:
    #            res = max(res, dfs(i, j, matrix, 0 , 2))
    #print(res)
