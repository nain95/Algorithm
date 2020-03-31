import sys
n = int(sys.stdin.readline())
result = 1
for _ in range(n):
    result += int(sys.stdin.readline()) -1
print(result)