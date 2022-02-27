import sys
from collections import defaultdict, deque

n, m = map(int, sys.stdin.readline().split())
dic = defaultdict(list)
# dic = [[] for _ in range(n+1)]
entry_level = [0] * (n + 1)
for _ in range(m):
    student1, student2 = map(int, sys.stdin.readline().split())
    dic[student1].append(student2)
    entry_level[student2] += 1
queue = deque()
for idx in range(1, n + 1):
    if entry_level[idx] == 0:
        queue.append(idx)
ans = []
for _ in range(1, n + 1):
    student_idx = queue.popleft()
    ans.append(student_idx)
    for idx in dic[student_idx]:
        entry_level[idx] -= 1
        if entry_level[idx] == 0:
            queue.append(idx)
for i in ans:
    print(i, end=' ')