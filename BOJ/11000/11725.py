import sys
from collections import defaultdict, deque

def bfs():
    queue = deque([1])
    while queue:
        length = len(queue)
        for _ in range(length):
            cur = queue.pop()
            for node in tree[cur]:
                if answer[node] == -1:
                    queue.append(node)
                    answer[node] = cur


n = int(sys.stdin.readline())
tree = defaultdict(list)
answer = [-1] * (n+1)
for _ in range(n-1):
    node1, node2 = map(int, sys.stdin.readline().split())
    tree[node1].append(node2)
    tree[node2].append(node1)
bfs()
for ans in answer[2:]:
    print(ans)