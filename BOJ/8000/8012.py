import sys
from _collections import deque


def check(i):
    result = []
    for z in range(1,n+1):
        if map_data[i][z] and visit[z] != 1:
            result.append(z)
    return result


n = int(sys.stdin.readline())
map_data = [[0]*(n+1) for _ in range(n+1)]
for _ in range(n-1):
    tmp = list(map(int,sys.stdin.readline().split()))
    map_data[tmp[0]][tmp[1]] = 1
    map_data[tmp[1]][tmp[0]] = 1
result = 0
m = int(sys.stdin.readline())
cur = 1
for _ in range(m):
    visit = [0] * (n + 1)
    city = int(sys.stdin.readline())
    cnt = 0
    queue = deque([cur])
    chk = True
    while chk:
        length = len(queue)
        for i in range(length):
            popdata = queue.popleft()
            visit[popdata] = 1
            if popdata == city:
                chk = False
                cur = city
                result += cnt
                break
            add = check(popdata)
            for z in add:
                queue.append(z)
        cnt+=1
        print(queue)
    print(result)
print(result)