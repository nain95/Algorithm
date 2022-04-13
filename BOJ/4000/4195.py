import sys
from collections import defaultdict

def find(x):
    while x != node[x]:
        x = node[x]
        node[x] = node[node[x]]
    return x

def union(x, y):
    x = find(x)
    y = find(y)
    if x != y:
        node[y] = x
        number[x] += number[y]

t = int(sys.stdin.readline())
answer = []
for _ in range(t):
    f = int(sys.stdin.readline())
    node = dict()
    number = defaultdict(lambda:1)
    idx = 0
    for _ in range(f):
        a, b = sys.stdin.readline().split()
        if a not in node:
            node[a] = a
        if b not in node:
            node[b] = b
        union(a, b)
        answer.append(str(number[find(a)]))
print("\n".join(answer))



