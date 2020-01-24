import sys
from _collections import deque
T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    N, M = map(int, sys.stdin.readline().rstrip().split())
    check = deque()
    for i in range(N):
        check.append(i)
    queue = deque(list(map(int, sys.stdin.readline().rstrip().split())))
    cnt = 0
    while 1:
        if max(queue) == queue[0]:
            cnt+=1
            queue.popleft()
            if check.popleft() == M:
                print(cnt)
                break
        else:
            queue.append(queue.popleft())
            check.append(check.popleft())
