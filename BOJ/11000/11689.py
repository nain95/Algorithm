import sys          # 오일러 파이함수
n = int(sys.stdin.readline())
result = n
p = 1
while p * p <= n:
    p += 1
    if n % p == 0:
        while n % p == 0:
            n //= p
        result *= (1.0 - (1.0 / p))
if n > 1:
    result *= (1.0 - (1.0 / n))
print(int(result))
