import sys,bisect

N = int(sys.stdin.readline())
res = [False]*22
for _ in range(N):
    cul = sys.stdin.readline().rstrip().split()
    if len(cul) == 2:
        num = int(cul[1])

    if cul[0] == 'add':
        if res[num] == False:
            res[num] = True
    elif cul[0] == 'remove':
        if res[num] == True:
            res[num] = False
    elif cul[0] == 'check':
        if res[num] == True:
            print(1)
        else:
            print(0)
    elif cul[0] == 'toggle':
        if res[num] == True:
            res[num] = False
        else:
            res[num] = True
    elif cul[0] == 'all':
        res = [True]*22
    elif cul[0] == 'empty':
        res = [False]*21
