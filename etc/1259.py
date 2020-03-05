import sys
while 1:
    num = list(map(int, list(sys.stdin.readline().rstrip())))
    if num == [0]:
        sys.exit()
    ans = 'yes'
    for i in range(len(num)//2):
        if num[i] != num[((i+1)*(-1))]:
            ans = 'no'
            break
    print(ans)
