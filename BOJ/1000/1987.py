import sys

r, c = map(int ,sys.stdin.readline().split())
# alp = [0] * 26
matrix = []
ans = 0
check = [['']*c for _ in range(r)]
for _ in range(r):
    matrix.append(list(sys.stdin.readline().rstrip()))
visited = [[0] * c for _ in range(r)]
stack = [(0, 0, 1, matrix[0][0])]
while stack:
    x, y, depth, string = stack.pop()
    if depth > ans:
        ans = depth
    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        nx, ny = dx + x, dy + y
        if 0 <= nx < r and 0 <= ny < c:
            if matrix[nx][ny] not in string:
                tmp = string +matrix[nx][ny]
                if check[nx][ny] != tmp:
                    check[nx][ny] = tmp
                    stack.append((nx, ny, depth+1, tmp))
print(ans)