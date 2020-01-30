import sys
import bisect
N = int(sys.stdin.readline().rstrip())
data = list(map(int,sys.stdin.readline().rstrip().split()))
lis = [data[0]]
for i in range(1,len(data)):
    if data[i] > lis[-1]:
        lis.append(data[i])
    else:
        idx = bisect.bisect_left(lis,data[i])
        lis[idx] = data[i]
print(len(lis))