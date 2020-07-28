import sys

num = int(sys.stdin.readline())
find = int(sys.stdin.readline())
result = [[0 for _ in range(num)] for _ in range(num)]
cnt = pow(num,2)
rep = num -1
for z in range(num):
    result[z][0] = cnt
    if find == cnt:
        answer = [z + 1,1]
    cnt -= 1
i,j = num-1,0   #현재 위치
h,w = 1,-1   #방향 1:++ -1:--
while cnt != 0:
    for x in range(rep):
        if h == 1:
            j += 1
        else:
            j -= 1
        result[i][j] = cnt
        if find == cnt:
            answer = [i+1,j+1]
        cnt -= 1
    for y in range(rep):
        if w == 1:
            i += 1
        else:
            i -= 1
        result[i][j] = cnt
        if find == cnt:
            answer = [i+1,j+1]
        cnt -= 1
    h *= -1
    w *= -1
    rep -= 1
for re in result:
    for r in re:
        print(f'{r} ',end='')
    print()
print(f'{answer[0]} {answer[1]}')