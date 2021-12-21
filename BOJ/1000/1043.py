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
    y = find(y)
    if x == y:
        return
    node[y] = x

N, M = list(map(int, sys.stdin.readline().split()))
whoKnowsTruth = list(map(int, sys.stdin.readline().split()))[1:]
parties = []
if len(whoKnowsTruth) == 0:
    for _ in range(M):
        party = (list(map(int, sys.stdin.readline().split())))
    print(M)
else:
    answer = 0
    node = {}
    for i in range(N):
        node[i+1] = i + 1
    for num in whoKnowsTruth:
        node[num] = whoKnowsTruth[0]
    for _ in range(M):
        party = (list(map(int, sys.stdin.readline().split())))
        for idx in range(1, len(party) - 1):
            union(party[idx], party[idx+1])
        parties.append(party[1:])
    for n in node:
        find(n)
    ans = set()
    for i in node.keys():
        ans.add(find(i))
    res = 0
    for i in parties:
        for j in i:
            if node[j] == node[whoKnowsTruth[0]]:
                break
        else:
            res += 1

    print(res)
