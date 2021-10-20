import sys

input_data = sys.stdin.readline().rstrip()
stack = []
dic = {'+': 0, '-': 0, '*': 1, '/': 1, '(' : 2, ')': 2}
for ch in input_data:
    if ch.isalpha():
        print(ch, end='')
    else:
        if not stack or ch == '(':
            stack.append(ch)
        elif ch == ')':
            while stack:
                tmp = stack.pop()
                if tmp == '(':
                    break
                print(tmp, end='')
        else:
            while stack and (dic[stack[-1]] >= dic[ch] and stack[-1] != '('):
                print(stack.pop(), end='')
            stack.append(ch)
while stack:
    print(stack.pop(), end='')