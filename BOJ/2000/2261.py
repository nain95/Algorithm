import sys,bisect
def length(A,B):        # 두 점 사이의 거리
    return (pow(A[0]-B[0],2)+pow(A[1]-B[1],2))
def solve(A):
    if len(A) <= 1:
        return 0
    elif len(A) ==2:
        return int(length(A[0],A[1]))
    elif len(A) == 3:
        a = int(length(A[0],A[1]))
        b = int(length(A[1],A[2]))
        c = int(length(A[0],A[2]))
        return min(a,min(b,c))
    mid = A[len(A)// 2][0]
    mid_index = len(A)// 2
    left_min = int(solve(A[:mid_index]))
    right_min = int(solve(A[mid_index:]))
    pt = 0
    if left_min < right_min:
        pt = left_min
    else:
        pt = right_min
    mid_data = []
    for i in range(len(A)) :
        if (mid - A[i][0])**2 <= pt :
            mid_data.append(A[i])
    mid_data = sorted(mid_data, key=lambda x: x[1])
    temp = pt
    if len(mid_data) >= 2:
        for i in range(len(mid_data) - 1):
            for j in range(i + 1, len(mid_data)):
                if (mid_data[j][1] - mid_data[i][1]) ** 2 >= pt:
                    break
                if mid_data[i][0] < mid and mid_data[j][0] < mid:
                    continue
                elif mid_data[i][0] > mid and mid_data[j][0] > mid:
                    continue
                leng = length(mid_data[i], mid_data[j])
                if leng < temp:
                    temp = leng
    return temp
N = int(sys.stdin.readline())
data = []
for _ in range(N):
    data.append(list(map(int,sys.stdin.readline().split())))
pa = len(data)
arr = list(set(map(tuple,data)))
aa = len(arr)
if pa != aa:
    print(0)
else:
    data.sort()
    print(solve(data))
