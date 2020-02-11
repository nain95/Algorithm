import sys
from _collections import deque
L,C = map(int,sys.stdin.readline().split())
data = sys.stdin.readline().split()
data.sort()
case_stack = deque(data[:C-L+1])


def count(t):
    case = ['a','e','i','o','u']
    check = 0
    for i in case:
        if t.count(i) >= 1:
            check=1
            t = t.replace(i,'')
    if check == 1 and len(t) >= 2:
        return True
    return False


def dfs(cur):
    global string
    case = []
    if cur == L:
        if count(string):
            print(string)
        return
    for i in range(data.index(string[-1])+1,C-L+1+cur):
        case.append(data[i])
    for j in range(len(case)):
        string += case[j]
        dfs(cur+1)
        string = string[:-1]


num = len(case_stack)
for _ in range(num):
    string = case_stack.popleft()
    dfs(1)
