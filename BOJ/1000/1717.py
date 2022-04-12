import sys

def find(x):
    if x == node[x]:
        return x
    # else:
    #     y = find(node[x])
    #     node[x] = y
    #     return y
    while x != node[x]:
        x = node[x]
        node[x] = node[node[x]]
    return x

def union(x,y):
    x = find(x)
    y = find(y)
    # if x == y:
    #     return
    if x <= y:
        node[y] = x
    else:
        node[x] = y

n, m = map(int, sys.stdin.readline().split())
# node = {}
answer = []
# for i in range(n + 1):
#     node[i] = i
node = [i for i in range(n+1)]
for _ in range(m):
    command, a, b = map(int, sys.stdin.readline().split())
    if command == 0:
        union(a, b)
    elif command == 1:
        if find(a) == find(b):
            # print('YES')
            answer.append("YES")
        else:
            # print('NO')
            answer.append("NO")
print('\n'.join(answer))