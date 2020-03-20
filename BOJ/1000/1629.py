import sys
A,B,C = map(int,sys.stdin.readline().split())
def solution(a,b):
    if b == 0:
        return 1
    elif b == 1:
        return a
    elif b %2 > 0:
        return solution(a,b-1)*a
    h = solution(a,b//2)
    h%=C
    return h**2 %C
print(solution(A,B) % C)