MOD = 1000000007
def POW(x, y):
    xy = 1
    while y > 0:
        if(y % 2) == 1:
            xy *= x
            y -= 1
            xy %= MOD
        x *= x
        x %= MOD
        y /= 2
    return xy

N, K = map(int, input().split())

r1 = 1
r2 = 1

for i in range(1, N+1):
    r1 *= i
    r1 %= MOD

for i in range(1, K+1):
    r2 *= i
    r2 %= MOD

for i in range(1, N-K+1):
    r2 *= i
    r2 %= MOD

r2 = POW(r2, MOD-2)
r2 %= MOD
r1 *= r2
r1 %= MOD
print(r1)