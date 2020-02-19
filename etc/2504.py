import sys
from _collections import deque
stack = []
temp = deque(list(sys.stdin.readline().rstrip()))
result = deque()
chk = 1
tmp = -1
result = 0
while temp:
    pop_data = temp.popleft()
    if pop_data == '(':
        tmp = 1
        stack.append(pop_data)
        chk*=2
    elif pop_data == '[':
        tmp = 2
        stack.append(pop_data)
        chk*=3
    elif stack == [] and pop_data == ')':
        print(0)
        sys.exit()
    elif stack == [] and pop_data == ']':
        print(0)
        sys.exit()
    elif stack[-1] == '(' and pop_data == ')':
        stack.pop()
        if tmp == 1:
            result += int(chk)
        chk /= 2
        tmp = -1
    elif stack[-1] == '[' and pop_data == ']':
        stack.pop()
        if tmp == 2:
            result += int(chk)
        chk /= 3
        tmp = -1

    else:
        print(0)
        sys.exit()
if stack:
    print(0)
    sys.exit()
print(result)