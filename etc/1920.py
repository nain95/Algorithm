import sys
N = int(sys.stdin.readline().rstrip())
N_data = list(map(int,sys.stdin.readline().rstrip().split()))
N_data = sorted(N_data)
M = int(sys.stdin.readline().rstrip())
M_data = list(map(int, sys.stdin.readline().rstrip().split()))
for i in M_data:
    start = 0
    end = N - 1
    while 1:
        mid = (start + end) // 2
        if start > end or end < start:
            print(0)
            break
        if i == N_data[mid]:
            print(1)
            break
        elif i > N_data[mid]:
            start = mid+1
        elif i < N_data[mid]:
            end = mid-1
