import sys


def solve(n):
    if n == 1 or n == 2:
        return 1
    a, b = [1,1]
    for i in range(n-2):
        tmp = a + b
        a = b
        b = tmp
    return b

print(solve(int(sys.stdin.readline())))