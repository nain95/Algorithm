N = int(input())
fibonacci_list = [0,1]+[-1] * (N-1)
def fibonacci(n):
    if fibonacci_list[n] != -1:
        return fibonacci_list[n]
    else:
        fibonacci_list[n] = fibonacci(n-1)+fibonacci(n-2)
    return fibonacci_list[n]
print(fibonacci(N))