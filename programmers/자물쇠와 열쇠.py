def rotate(m):
    n = len(m)
    ret = [[0] * n for _ in range(n)]
    for r in range(n):
        for c in range(n):
            ret[c][n-1-r] = m[r][c]
    return ret


def solution(key, lock):
    answer = True
    n = len(lock)
    m = len(key)-1
    lock_count = [element for l in lock for element in l].count(0)
    for _ in range(4):
        key = rotate(key)
        for x in range(m,-1,-1):
            for y in range(m,-1,-1):
                start = [x,y]
                for i in range(n-1):
                    for j in range(n-1):
                        start[0] += i



    return answer

print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]],[[1, 1, 1], [1, 1, 0], [1, 0, 1]]))