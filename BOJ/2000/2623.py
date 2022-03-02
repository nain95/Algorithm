import sys
from collections import defaultdict, deque

n, m = map(int, sys.stdin.readline().split())
singer_path = defaultdict(list)
path_cnt = [0] * (n + 1)
for _ in range(m):
    singer = tuple(map(int, sys.stdin.readline().split()))
    for idx in range(1, singer[0]):
        singer_path[singer[idx]].append(singer[idx + 1])
        path_cnt[singer[idx + 1]] += 1
queue = deque()
for i in range(1, n+1):
    if path_cnt[i] == 0:
        queue.append(i)
answer = []
for _ in range(n):
    if not queue:
        answer = [0]
        break
    cur = queue.popleft()
    answer.append(cur)
    for idx in singer_path[cur]:
        path_cnt[idx] -= 1
        if path_cnt[idx] == 0:
            queue.append(idx)
for i in answer:
    print(i)


