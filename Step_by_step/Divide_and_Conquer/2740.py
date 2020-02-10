import sys
def mul(a,b):
    ans = 0
    for i in range(len(a)):
        ans += a[i]*b[i]
    return ans

AN,AM = map(int,sys.stdin.readline().split())
A = []
A_data = []
for i in range(AN):
    A.append(list(map(int,sys.stdin.readline().split())))
    A_data.append(A[i][0:AM])
BN,BM = map(int,sys.stdin.readline().split())
B = []
for _ in range(BN):
    B.append(list(map(int,sys.stdin.readline().split())))
B_data = []
tmp = []
for j in range(BM):
    for p in range(BN):
        tmp.append(B[p][j])
    B_data.append(tmp)
    tmp = []
result = [[0]*BM for _ in range(AN)]
for z in range(AN):
    for q in range(BM):
        result[z][q] = mul(A_data[z],B_data[q])
for w in result:
    for n in w:
        print(n,end=' ')
    print('')