import sys
import bisect
N,M = map(int,sys.stdin.readline().rstrip().split())
data = list(map(int,sys.stdin.readline().split()))
data = sorted(data)
left = 0
right = data[-1]
max = 0
while left <= right:
    mid = (left+right)//2
    idx = bisect.bisect_left(data,mid)
    len = 0
    for i in range(idx,N):
        len += data[i] - mid
    if len >= M:
        if max < mid:
            max = mid
        left = mid+1
    else:
        right = mid-1
print(max)
