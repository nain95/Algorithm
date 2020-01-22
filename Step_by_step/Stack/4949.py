import sys
while 1:
    stack = []
    string = sys.stdin.readline().rstrip()
    if string == '.':
        break
    answer = "yes"
    for i in string:
        if i == '(' or i == '[':
            stack.append(i)
        if i==')':
            if stack == []:
                answer = 'no'
                break
            tmp = stack.pop()
            if tmp != '(':
                answer = 'no'
                break
        elif i == ']':
            if stack == []:
                answer = 'no'
                break
            tmp = stack.pop()
            if tmp != '[':
                answer = 'no'
                break

    if stack != []:
        answer = 'no'
    print(answer)
