import sys
num = int(sys.stdin.readline().rstrip())
for i in range(num):
    case = list(map(int,(sys.stdin.readline().rstrip().split())))
    if case[0] < 12 or case[1] < 4:
        print(-1)
    else:
        result = case[1]*11+4
        print(result)