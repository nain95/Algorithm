import sys,bisect
N,C = map(int,sys.stdin.readline().split())
data = []
for _ in range(N):
    data.append(int(sys.stdin.readline()))
data = sorted(data)
home= []
left = 1
right = data[-1] - data[0]
min = 1000000000
answer = 0
while left <= right:
    mid = (left+right)//2
    tmp = 0
    while tmp < len(data):
        home.append(data[tmp])
        tmp = bisect.bisect_left(data,data[tmp]+mid)
    if len(home) >= C:
        answer = mid
        left = mid+1
        home = []
    else:
        home = []
        right = mid-1
print(answer)
