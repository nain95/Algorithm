import sys

n = int(sys.stdin.readline())
answer = [[float('inf')] * n for _ in range(n)]
matrix = []
for _ in range(n):
    matrix.append(list(map(int, sys.stdin.readline().split())))
for i in range(n):
    for j in range(n):
        if matrix[i][j]:
            answer[i][j] = matrix[i][j]

for i in range(n):
    for j in range(n):
        for z in range(n):
            if answer[j][i] + answer[i][z] < answer[j][z]:
                answer[j][z] = answer[j][i] + answer[i][z]
for a in answer:
    for number in a:
        if number != float('inf'):
            print(1, end=" ")
        else:
            print(0, end=" ")
    print()