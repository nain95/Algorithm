import sys
from collections import deque

string1 = list(sys.stdin.readline().rstrip())
string2 = list(sys.stdin.readline().rstrip())
matrix = [[0] * (len(string2) + 1) for _ in range(len(string1) + 1)]
for i, str1 in enumerate(string1):
    i += 1
    for j, str2 in enumerate(string2):
        j += 1
        if str1 == str2:
            matrix[i][j] = matrix[i-1][j-1] + 1
        else:
            matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1])
queue = deque()
while matrix[i][j] != 0:
    if matrix[i][j] == matrix[i-1][j]:
        i -= 1
    elif matrix[i][j] == matrix[i][j-1]:
        j -= 1
    else:
        queue.appendleft(string1[i-1])
        i -= 1
        j -= 1
print(len(queue))
print("".join(queue))