import sys

def check(S,E):
    global one_cnt,zero_cnt
    if S==E:
        if data[S[0]][S[1]] == 1:
            print(1,end='')
            return
        else:
            print(0,end='')
            return
    ck = (E[0]-S[0]+1)*(E[1]-S[1]+1)
    w,b = 0,0
    for i in range(E[0]-S[0]+1):
        w += data[S[0]+i][S[1]:E[1]+1].count(0)
        b += data[S[0]+i][S[1]:E[1]+1].count(1)
    if w == ck:
        print(0,end='')
        return
    elif b == ck:
        print(1,end='')
        return
    else:
        print('(',end='')
        check(S,[(E[0]+S[0])//2,(E[1]+S[1])//2])
        check([S[0],(E[1]+S[1])//2+1],[(E[0]+S[0])//2,E[1]])
        check([(E[0]+S[0])//2+1,S[1]],[E[0],(E[1]+S[1])//2])
        check([(E[0]+S[0])//2+1,(E[1]+S[1])//2+1],E)
        print(')', end='')
N = int(sys.stdin.readline())
data = []
for _ in range(N):
    data.append(list(map(int,list(sys.stdin.readline().rstrip()))))
one_cnt,zero_cnt = 0,0
check([0,0],[N-1,N-1])
