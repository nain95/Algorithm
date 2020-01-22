import sys
N = int(sys.stdin.readline().rstrip())
pop = []
data = []
num = []
stack = []
result = []
for i in range(N):
    data.append(int(sys.stdin.readline().rstrip()))
    num.append(N-i)
for j in data:
    if j in pop:
        print("NO")
        sys.exit()
    while 1:
        if stack != []:
            if stack[-1] == j:
                result.append('-')
                stack.pop()
                break
            else:
                if num == []:
                    print("NO")
                    sys.exit()
                tmp_pop = num.pop()
                stack.append(tmp_pop)
                result.append('+')
        else:
            if num == []:
                print("NO")
                sys.exit()
            tmp_pop = num.pop()
            stack.append(tmp_pop)
            result.append('+')
for res in result:
    print(res)