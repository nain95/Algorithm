import sys
from collections import deque

def D(num):
    return (num * 2) % 10000

def S(num):
    num -= 1
    if num == -1:
        num = 9999
    return num

def L(num):
    tmp = int(num / 1000)
    num = num % 1000 * 10 + tmp
    return num

def R(num):
    tmp = num % 10
    num = int(num / 10) + (tmp * 1000)
    return num

def bfs():
    queue = deque([[a, '']])
    command = [D,S,L,R]
    visited = {a : True}
    while deque:
        cur, cur_command = queue.popleft()
        if cur == b:
            return cur_command
        for k in range(4):
            command_cur = command[k](cur)
            if command_cur not in visited:
                if command_cur == b:
                    return cur_command + dic[k]
                visited[command_cur] = True
                queue.append([command_cur, cur_command + dic[k]])

n = int(sys.stdin.readline())
dic = {0: 'D', 1: 'S', 2: 'L', 3: 'R'}
for _ in range(n):
    a,b = list(map(int, sys.stdin.readline().split()))
    res = bfs()
    print(res)