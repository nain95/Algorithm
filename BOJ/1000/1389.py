import sys
from collections import defaultdict, deque

def bfs(dic, user1, user2):
    res = 0
    queue = deque([user1])
    visited = [-1] * (N + 1)
    while (queue):
        cnt = len(queue)
        for _ in range(cnt):
            cur = queue.popleft()
            if cur == user2:
                return res
            visited[cur] = 1
            for user in dic[cur]:
                if visited[user] == -1:
                    queue.append(user)
        res += 1

N, M = map(int, sys.stdin.readline().split())
dic = defaultdict(list)
ans = [-1, sys.maxint]
for _ in range(M):
    user1, user2 = map(int, sys.stdin.readline().split())
    dic[user1].append(user2)
    dic[user2].append(user1)
for i in range(1, N + 1):
    num = 0
    for j in range(1, N + 1):
        if i == j:
            continue
        num += bfs(dic, i, j)
    if num < ans[1]:
        ans[0] = i
        ans[1] = num
print(ans[0])
