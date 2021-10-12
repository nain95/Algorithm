import sys
from collections import deque

def bfs(a):
    queue = deque([a])
    cnt = 0
    func = [lambda x:x * 2, lambda x: x * 10 + 1]
    while queue:
        cnt += 1
        length = len(queue)
        for _ in range(length):
            cur = queue.popleft()
            if cur == b:
                return (cnt)
            for f in func:
                if f(cur) <= b:
                    queue.append(f(cur))
    return -1

a, b = map(int, sys.stdin.readline().split())
print(bfs(a))
