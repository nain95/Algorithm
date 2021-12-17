import sys

def find(x):
    if x == node[x]:
        return x
    else:
        y = find(node[x])
        node[x] = y
        return y

def union(x,y):
    x = find(x)
    y = find(x)

    if x == y:
        return

    node[y] = x

N, M = list(map(int, sys.stdin.readline().split()))
whoKnowsTruth = list(map(int, sys.stdin.readline().split()))
parties = []
if whoKnowsTruth[0] == 0:
    for _ in range(M):
        party = (list(map(int, sys.stdin.readline().split())))
    print(M)
else:
    answer = 0
    node = {}
    for num in whoKnowsTruth[1:]:
        node[num] = whoKnowsTruth[1]
    for _ in range(M):
        party = (list(map(int, sys.stdin.readline().split())))
        for num in node.keys():
            if num in party[1:]:
                for new in party:
                    if new not in node:
                        node[new] = new
                        union(num, new)
                break
        else:
            for num in party[1:]:
                node[num] = party[1]
    ans = set()
    for i in node.keys():
        ans.add(find(i))
    print(len(ans) - 1)
