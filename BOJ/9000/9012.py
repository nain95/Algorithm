import sys

number = int(sys.stdin.readline().rstrip())
for i in range(number):
    tmp = 0
    string = list(sys.stdin.readline())
    for j in range(len(string)):
        if tmp <0:
            break
        if string[j] =='(':
            tmp = tmp+1
        elif string[j] ==')':
            tmp = tmp -1
    if tmp == 0:
        print("YES")
    else:
        print("NO")