import sys

n = int(sys.stdin.readline())
num = []
i = round(n * 0.15)
for _ in range(n):
    num.append(int(sys.stdin.readline()))
num = sorted(num)
z = max(1, n-i-i)
print(round(sum(num[i:n-i]) / z))
