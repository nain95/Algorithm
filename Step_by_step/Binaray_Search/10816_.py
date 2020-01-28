import sys
import bisect
N = int(sys.stdin.readline().rstrip())
n_data = list(map(int,sys.stdin.readline().rstrip().split()))
M = int(sys.stdin.readline().rstrip())
m_data = list(map(int,sys.stdin.readline().rstrip().split()))
n_data = sorted(n_data)
for i in range(M):
    idx1=bisect.bisect_left(n_data,m_data[i])
    if idx1 <len(n_data) and n_data[idx1]==m_data[i]:
        idx2=bisect.bisect_left(n_data,m_data[i]+1)
        print(idx2-idx1,end=' ')
    else:
        print(0,end=' ')