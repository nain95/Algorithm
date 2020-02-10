import sys

def check(S,E):
    global W_cnt,B_cnt
    if S==E:
        if data[S[0]][S[1]] == 1:
            B_cnt+=1
            return
        else:
            W_cnt+=1
            return
    ck = (E[0]-S[0]+1)*(E[1]-S[1]+1)
    w,b = 0,0
    for i in range(E[0]-S[0]+1):
        w += data[S[0]+i][S[1]:E[1]+1].count(0)
        b += data[S[0]+i][S[1]:E[1]+1].count(1)
    if w == ck:
        W_cnt += 1
        return
    elif b == ck:
        B_cnt += 1
        return
    else:
        check(S,[(E[0]+S[0])//2,(E[1]+S[1])//2])
        check([S[0],(E[1]+S[1])//2+1],[(E[0]+S[0])//2,E[1]])
        check([(E[0]+S[0])//2+1,S[1]],[E[0],(E[1]+S[1])//2])
        check([(E[0]+S[0])//2+1,(E[1]+S[1])//2+1],E)
N = int(sys.stdin.readline())
data = []
for _ in range(N):
    data.append(list(map(int,sys.stdin.readline().split())))
W_cnt,B_cnt = 0,0
check([0,0],[N-1,N-1])
print(W_cnt)
print(B_cnt)