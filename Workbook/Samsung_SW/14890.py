import sys
N,L = map(int,sys.stdin.readline().split())
data = []
cnt = 0
for k in range(N):
    temp = list(map(int,sys.stdin.readline().split()))
    data.append(temp)
    c = True
    if temp.count(temp[0]) == N:
        cnt+=1
    else:
        check = 1
        check_down = 0
        cur = temp[0]
        cnt+=1
        for i in range(1,N):
            if check_down >= L and cur == temp[i]:
                check_down = 0
                check+=1
            elif cur == temp[i] and check_down >= 1:
                check_down += 1
            elif cur == temp[i]:
                check += 1
            elif cur + 1 == temp[i] and check >= L:
                check = 1
            elif cur - 1 == temp[i] and (check_down >= L or check_down == 0):
                check_down += 1
                check = 0
            else:
                cnt-=1
                c = False
                break
            cur = temp[i]
        if c and check_down < L and check_down != 0:
            cnt-=1
data_B = [list(x) for x in zip(*data)]    # 행렬 대치
for temp in data_B:
    c = True
    if temp.count(temp[0]) == N:
        cnt+=1
    else:
        check = 1
        check_down = 0
        cur = temp[0]
        cnt+=1
        for i in range(1,N):
            if check_down >= L and cur == temp[i]:
                check_down = 0
                check+=1
            elif cur == temp[i] and check_down >= 1:
                check_down += 1
            elif cur == temp[i]:
                check += 1
            elif cur + 1 == temp[i] and check >= L:
                check = 1
            elif cur - 1 == temp[i] and (check_down >= L or check_down == 0):
                check_down += 1
                check = 0
            else:
                c= False
                cnt-=1
                break
            cur = temp[i]
        if c and check_down < L and check_down != 0:
            cnt-=1
print(cnt)