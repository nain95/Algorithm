import sys

def power(a,b,c):
    if b == 0:
        return 1
    elif b == 1:
        return a
    elif b %2 > 0:
        return power(a, b-1, c) * a
    h = power(a, b//2, c)
    h %= c
    return h**2 % c

n = int(sys.stdin.readline())
tmp = 0
for _ in range(n):
    B, A = map(int, sys.stdin.readline().split())
    tmp += (A * power(B,1000000005, 1000000007) % 1000000007)
    tmp %= 1000000007
print(tmp)


