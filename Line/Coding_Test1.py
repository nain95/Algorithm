import sys,time
from _collections import deque

def bfs(cnt):
    global c,b,queue
    while 1:
        if c > 2000000:
            return -1
        if c in queue:
            return cnt
        for i in range(len(queue)):
            cur = queue.popleft()
            for k in range(3):
                if k == 0:
                    tmp_cur = cur * 2
                elif k == 1:
                    tmp_cur = cur + 1
                else:
                    tmp_cur = cur - 1
                if 0 <= tmp_cur <= 200000:
                    queue.append(tmp_cur)
        queue = deque(list(set(queue)))
        cnt += 1
        c += cnt

c,b = map(int,sys.stdin.readline().split())
start = time.time()
queue = deque([b])
print(bfs(0))
print(time.time() - start)