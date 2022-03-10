from collections import defaultdict, deque
import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n, k = map(int, sys.stdin.readline().split())
    build_time = [0]+list(map(int, sys.stdin.readline().split()))
    build_dic = defaultdict(list)
    entry_level = [0] * (n + 1)
    dp = [0] * (n + 1)
    queue = deque()
    for _ in range(k):
        first, second = map(int, sys.stdin.readline().split())
        build_dic[first].append(second)
        entry_level[second] += 1
    for i in range(1, n + 1): 
        if entry_level[i] == 0:
            queue.append(i)
            dp[i] = build_time[i]
    while queue:
        now = queue.popleft()
        for i in build_dic[now]: 
            entry_level[i] -= 1 
            dp[i] = max(dp[now] + build_time[i], dp[i])
            if entry_level[i] == 0: 
                queue.append(i)
    ans = int(sys.stdin.readline())
    print(dp[ans])

