import sys
n = int(sys.stdin.readline().rstrip())
stack = []

for i in range(n):
    code = list(sys.stdin.readline().rstrip().split())
    if code[0] == 'push':
        stack.append(code[1])
    elif code[0] =='top':
        try:
            print(stack[-1])
        except IndexError:
            print("-1")
    elif code[0] == 'pop':
        try:
            print(stack[-1])
            stack.pop()
        except IndexError:
            print("-1")
    elif code[0] == 'size':
        print(len(stack))
    elif code[0] == 'empty':
        if len(stack)==0:
            print("1")
        else:
            print("0")


