import sys


def solve(n, r, c, result=0):
    if n == 2:
        if r == 0 and c == 0:
            pass
        elif r == 0 and c == 1:
            result += 1
        elif r == 1 and c == 0:
            result += 2
        else:
            result += 3
        print(result)
        return
    if r >= n//2 and c >= n//2:
        solve(n//2, r - n//2, c - n//2, result + 3 * pow(n//2, 2))
    elif r >= n//2:
        solve(n//2, r - n//2, c, result + 2 * pow(n//2, 2))
    elif c >= n//2:
        solve(n//2, r, c - n//2, result + pow(n//2, 2))
    else:
        solve(n//2, r, c,result)

N, r, c = map(int,sys.stdin.readline().split())
N = pow(2,N)
solve(N,r,c)