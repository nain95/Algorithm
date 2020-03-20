import sys

def check(S,E):
    global minus_cnt,zero_cnt,one_cnt
    if S==E:
        if data[S[0]][S[1]] == 1:
            one_cnt+=1
            return
        elif data[S[0]][S[1]] == -1:
            minus_cnt+=1
            return
        else:
            zero_cnt+=1
            return
    ck = (E[0]-S[0]+1)*(E[1]-S[1]+1)
    m,z,o = 0,0,0
    for i in range(E[0]-S[0]+1):
        m += data[S[0]+i][S[1]:E[1]+1].count(-1)
        z += data[S[0]+i][S[1]:E[1]+1].count(0)
        o += data[S[0]+i][S[1]:E[1]+1].count(1)
    if z == ck:
        zero_cnt += 1
        return
    elif m == ck:
        minus_cnt += 1
        return
    elif o == ck:
        one_cnt += 1
        return
    else:
        length = (E[0]-S[0]+1)//3
        check(S,[S[0]+length-1,S[1]+length-1])
        check([S[0],S[1]+length],[S[0]+length-1,S[1]+length+length-1])
        check([S[0],S[1]+length*2],[S[0]+length-1,S[1]+length*3-1])
        check([S[0]+length,S[1]],[S[0]+length*2-1,S[1]+length-1])
        check([S[0]+length,S[1]+length],[S[0]+length*2-1,S[1]+length+length-1])
        check([S[0]+length,S[1]+length*2],[S[0]+length*2-1,E[1]])
        check([S[0] + length*2, S[1]],[E[0],S[1]+length-1])
        check([S[0] + length*2, S[1] + length], [E[0], S[1] + length + length - 1])
        check([S[0] + length * 2, S[1] + length*2],E)
N = int(sys.stdin.readline())
data = []
for _ in range(N):
    data.append(list(map(int,sys.stdin.readline().split())))
minus_cnt,zero_cnt,one_cnt = 0,0,0
check([0,0],[N-1,N-1])
print(minus_cnt)
print(zero_cnt)
print(one_cnt)