import sys

num1 = int(sys.stdin.readline())
num2 = int(sys.stdin.readline())
print(max(num1,num2) + max(num1-num2, num2-num1))