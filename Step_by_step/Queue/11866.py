import sys
from _collections import deque
N,K= map(int,sys.stdin.readline().rstrip().split())
queue = []
for n in range(1,N+1):
    queue.append(n)
result = []
pop_index = (K-1)%N
for i in range(N):
    result.append(queue.pop(pop_index))
    if N-i-1 != 0:
        pop_index = (pop_index+K-1)%(N-i-1)
print('<',end='')
for tmp in result[0:-1]:
    print(tmp,end=', ')
print(result[-1],end='')
print('>')

