import sys
from _collections import deque
N = int(sys.stdin.readline().rstrip())
queue = deque()
for n in range(N,0,-1):
    queue.append(n)
for _ in range(N-1):
    queue.pop()
    queue.appendleft(queue.pop())
print(queue[0])