import sys
N = int(sys.stdin.readline())
K = int(sys.stdin.readline())
left = 1
right = K
while left <= right:
    mid = (left+right)//2
    cnt = 0
    for i in range(1,N+1):
        cnt += min(mid//i,N)
    if K == cnt:
        ans = mid
        right = mid-1
    elif K > cnt:
        left = mid + 1
    elif K<cnt:
        ans = mid
        right = mid -1
print(ans)