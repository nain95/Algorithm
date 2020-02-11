import sys
def mod(A):
    for i in range(len(A)):
        for j in range(len(A[0])):
            A[i][j] = A[i][j] % MOD
    return A
def mul_data(a,b):
    ans = 0
    for i in range(len(a)):
        ans += a[i]*b[i]
    return ans

def mul(A,B):
    #print(A)
    #print(B)
    AN = len(A)
    AM = len(A[0])
    A_data = []
    for i in range(AN):
        A_data.append(A[i][0:AM])
    BN, BM = len(B),len(B[0])
    B_data = []
    tmp = []
    for j in range(BM):
        for p in range(BN):
            tmp.append(B[p][j])
        B_data.append(tmp)
        tmp = []
    result = [[0] * BM for _ in range(AN)]
    for z in range(AN):
        for q in range(BM):
            result[z][q] = mul_data(A_data[z], B_data[q])
    return result

def solution(a,b):
    if b == 0:
        tmp = []
        return_data = []
        for i in range(len(a)):
            for j in range(len(a[i])):
                tmp.append(1)
            return_data.append(tmp)
            tmp = []
        return return_data
    elif b == 1:
        return a
    elif b %2 > 0:
        return mod(mul(solution(a,b-1),a))
    h = mod(solution(a,b//2))
    return mod(mul(h,h))
MOD = 1000
N,B = map(int,sys.stdin.readline().split())
A = []
for _ in range(N):
    A.append(list(map(int,sys.stdin.readline().split())))
result = solution(A,B)
for i in result:
    for j in i:
        print(j%MOD,end=' ')
    print('')