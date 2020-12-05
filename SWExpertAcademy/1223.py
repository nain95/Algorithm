def postfix(expression):
    stack = []
    for element in expression:
        if element == '+':
            op2 = stack.pop()
            op1 = stack.pop()
            stack.append(op1 + op2)
        elif element == '*':
            op2 = stack.pop()
            op1 = stack.pop()
            stack.append(op1 * op2)
        else:
            stack.append(int(element))
    return stack

def is_number(x):
    if x not in operator:
        return True
    else:
        return False

operator = {'*':1, '+':0}
for index in range(10):
    postfix_data = ''
    stack = []
    n = int(input())
    data = input()
    for d in data:
        if is_number(d):
            postfix_data += d
        else:
            while stack:
                if operator[stack[-1]] <= operator[d]:
                    break
                postfix_data += stack.pop()
            stack.append(d)
    while stack:
        postfix_data += stack.pop()
    print(f'#{index+1} {postfix(postfix_data)[0]}')