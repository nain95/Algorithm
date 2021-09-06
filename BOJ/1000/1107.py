import sys

def solve(check, num1, num2):
    chk = 0
    for i in range(len(num1)):
        if check[int(num1[i])] == 1:
            break
    else:
        chk += 1

    for j in range(len(num2)):
        if check[int(num2[j])] == 1:
            break
    else:
        chk += 2

    if chk == 0:
        return -1
    elif chk == 1:
        return int(num1)
    elif chk == 2:
        return int(num2)
    else:
        if len(num1) < len(num2):
            return int(num1)
        else:
            return int(num2)

num = int(sys.stdin.readline())
m = int(sys.stdin.readline())
trouble = list(map(int, sys.stdin.readline().split()))
check = [-1] * 11
for t in trouble:
    check[t] = 1
ans = 0
num1 = num
num2 = num
c = -1
if solve(check, str(num), str(num)) != -1:
    print(min(abs(100 - num), len(str(num))))
else:
    while m != 10:
        num1 += 1
        num2 -= 1
        if num2 < 0:
            num2 = 0
        ans += 1
        c = solve(check, str(num1), str(num2))
        if c != -1:
            break
    if c == -1:
        print (abs(100 - num))
    else:
        print(min(abs(100 - num), ans + len(str(c))))
