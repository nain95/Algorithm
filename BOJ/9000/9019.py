import sys
from collections import deque

def D(num):
    num = int(num)
    num = (num * 2) % 10000
    num = str(num)
    while len(num) != 4:
        num = '0' + num
    return num

def S(num):
    num = int(num) - 1
    if num == -1:
        num = 9999
    num = str(num)
    while len(num) != 4:
        num = '0' + num
    return num

def L(num):
    num = list(num)
    tmp = num[0]
    num[0] = num[1]
    num[1] = num[2]
    num[2] = num[3]
    num[3] = tmp
    return "".join(num)

def R(num):
    num = list(num)
    tmp = num[3]
    num[3] = num[2]
    num[2] = num[1]
    num[1] = num[0]
    num[0] = tmp
    return "".join(num)

def bfs():
    temp = a
    queue = deque([a])
    command = [D,S,L,R]
    dp = []
    while deque:
        length = len(queue)
        dp.append([])
        for _ in range(length):
            cur = queue.popleft()
            if cur == b:
                return dp
            for k in range(4):
                queue.append(command[k](cur))
                dp[-1].append(command[k](cur))

n = int(sys.stdin.readline())
dic = {0: 'D', 1: 'S', 2: 'L', 3: 'R'}
for _ in range(n):
    a,b = sys.stdin.readline().split()
    while len(a) != 4:
        a = '0' + a
    while len(b) != 4:
        b = '0' + b
    res = bfs()
    for r in res:
        print(r, end='')
    print()
