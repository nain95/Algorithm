import sys
import bisect
N = int(sys.stdin.readline().rstrip())
data = list(map(int,sys.stdin.readline().rstrip().split()))
lis = [data[0]]
idx_list = [0]
for i in range(1,len(data)):
    if data[i] > lis[-1]:
        lis.append(data[i])
        idx_list.append(len(lis)-1)
    else:
        idx = bisect.bisect_left(lis,data[i])
        lis[idx] = data[i]
        idx_list.append(idx)
print(len(lis))
stack = []
temp = len(lis)-1
for i in range(N-1,-1,-1):
    if idx_list[i] == temp:
        stack.append(data[i])
        temp-=1
for _ in range(len(stack)):
    print(stack.pop(),end=' ')