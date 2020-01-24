import sys
from _collections import deque
T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    exit = True
    P = list(sys.stdin.readline().rstrip())
    n = int(sys.stdin.readline().rstrip())
    data = sys.stdin.readline().rstrip()
    if data == '[]' and P.count('D')>0:
        print('error')
        continue
    elif data != '[]':
        data = deque(list(map(int, data[1:-1].split(','))))
    elif data == '[]':
        data = deque()
    if P.count('D') > n:
        print('error')
        continue
    check = 0
    for i in P:
        if i == 'R':
            if check == 0:
                check = 1
            else:
                check = 0
        else:
            if check == 1:
                data.pop()
            else:
                data.popleft()
    if P.count('R')%2!= 0:
        data.reverse()
    if len(data) == 0:
        print([])
    else:
        print('[',end='')
        for i in range(len(data)-1):
            print(data[i],end=',')
        print(data[-1],end=']\n')
