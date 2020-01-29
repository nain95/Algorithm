import sys
def binary_search(left,right):
    result = []
    while left<=right:
        cnt = 0
        mid = (left+right)//2
        if mid == 0:
            return 1
        for i in data:
            cnt+=i//mid
        if cnt >= N:
            result.append(mid)
            left = mid+1
        elif cnt < N:
            right = mid-1
    return max(result)
K,N = map(int,sys.stdin.readline().split())
data =[]
for _ in range(K):
    data.append(int(sys.stdin.readline().rstrip()))
data = sorted(data)
print(binary_search(0,data[-1]))