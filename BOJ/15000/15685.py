import sys

answer = 0
dragon = [[0,1],[-1,0],[0,-1],[1,0]]
matrix = [[0]*101 for _ in range(101)]
n = int(sys.stdin.readline())
for _ in range(n):
    y, x, d, g = list(map(int,sys.stdin.readline().split()))
    stack = [d]
    matrix[x][y] = 1
    for _ in range(g):
        for tmp in stack[::-1]:
            stack.append((tmp+1) % 4)
    for s in stack:
        x, y = x + dragon[s][0], y + dragon[s][1]
        matrix[x][y] = 1
for i in range(100):
    for j in range(100):
        if matrix[i][j] and matrix[i+1][j] and matrix[i][j+1] and matrix[i+1][j+1]:
            answer += 1
print(answer)




