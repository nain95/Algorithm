import sys
N = int(sys.stdin.readline())
mod = 1000000
p = 1500000
fibo = [0,1]+[0]*p
for i in range(2,p):
    fibo[i] = fibo[i-1] + fibo[i-2]
    fibo[i] %= mod
print(fibo[N%p])