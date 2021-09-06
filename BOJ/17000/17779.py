import sys

def first(x, y, d1, d2):
    cnt = 0
    for r in range(1, x + d1):
        for c in range(1, y + 1 + min(0 , x-r-1)):
            cnt += matrix[r-1][c-1]
    return cnt

def second(x, y, d1, d2):
    cnt = 0
    for r in range(1, x + d2 + 1):
        for c in range(y + 1 - min(0, x-r), n + 1):
            cnt += matrix[r-1][c-1]
    return cnt

def third(x, y, d1, d2):
    cnt = 0
    for r in range(x + d1, n + 1):
        for c in range(1, y - d1 + r - (x+d1)):
            if c >= y - d1 + d2:
                break
            cnt += matrix[r-1][c-1]
    return cnt
    
def fourth(x, y, d1, d2):
    cnt = 0
    for r in range(x + d2 + 1, n + 1):
        for c in range(y + d2 - (r - (x + d2 + 1)),n + 1):
            if c < y - d1 + d2:
                continue
            cnt += matrix[r-1][c-1]
    return cnt

def solve(x, y, d1, d2):
    cnt = [0] * 5
    cnt[0] = first(x, y, d1, d2)
    cnt[1] = second(x, y, d1, d2)
    cnt[2] = third(x, y, d1, d2)
    cnt[3] = fourth(x, y, d1, d2)
    cnt[4] = sum_matrix - sum(cnt)
    return (max(cnt) - min(cnt))


n = int(sys.stdin.readline())
matrix = []
sum_matrix = 0
for _ in range(n):
    matrix.append(list(map(int, sys.stdin.readline().split())))
    sum_matrix += sum(matrix[-1])
ans = sum_matrix
for x in range(1, n - 1):
    for y in range(2, n):
        for d1 in range(1, n):
            if y - d1 < 1:
                break
            for d2 in range(1, n):
                if y + d2 > n or x + d1 + d2 > n:
                    break
                ans = min(ans, solve(x, y, d1, d2))
print(ans)
