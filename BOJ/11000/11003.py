import sys
from _collections import deque
N,L = map(int,sys.stdin.readline().split())
A = list(map(int,sys.stdin.readline().split()))
deque = deque()
for i in range(N):
    while deque and deque[0][1] <= i-L:
        deque.popleft()
    while deque and deque[-1][0] >= A[i]:
        deque.pop()

    deque.append([A[i],i])
    sys.stdout.write(str(deque[0][0])+" ")