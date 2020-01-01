def Fibonacci(N):
    if N == 0:
        return 0
    elif N == 1:
        return 1
    elif N==2:
        return 1
    else:
        return Fibonacci(N-1) + Fibonacci(N-2)
num = int(input())
print(Fibonacci(num))