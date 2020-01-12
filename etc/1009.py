import sys
t = int(sys.stdin.readline().rstrip())
for i in range(t):
    a,b = list(map(int,sys.stdin.readline().split()))
    b%=4
    if b != 0:
        c = pow(a,b)
    else:
        c=pow(a,4)
    if str(c)[-1] == '0':
        print(10)
    else:
        print(str(c)[-1])