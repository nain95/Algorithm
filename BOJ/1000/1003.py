num0 = [1,0]
num1 = [0,1]

i = int(input())

memo = {0:0, 1:1}

def fibonacci(n):
    global num0
    global num1

    if n == 0:
        return 0
    elif n == 1:
        return 1
    if n not in memo:
        memo[n] = fibonacci(n-1) +fibonacci(n-2)

    return memo[n]

for j in range(0,i):
    n = int(input())
    if n >len(num1)-1:
        for i in range(len(num0), n+1):
            num0.append(num0[i - 2] + num0[i - 1])
            num1.append(num1[i - 2] + num1[i - 1])

    print(str(num0[n])+" "+str(num1[n]))