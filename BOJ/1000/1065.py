import sys
def num(N):
    if N < 100:
        return 1
    else:
        num1 = int(N/100)
        num2 = int(N%100/10)
        num3 = int(N%10)
        if num1-num2 == num2 - num3:
            return 1
        else:
            return 0

input_num = int(sys.stdin.readline().rstrip())
result = 0
for i in range(1,input_num+1):
    if num(i):
        result += 1
print(result)
