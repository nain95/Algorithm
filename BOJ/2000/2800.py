import sys,itertools
data = list(sys.stdin.readline().rstrip())
stack = []
result = []
result_data = []
for i in range(len(data)):
    if data[i] == '(':
        stack.append(['(',i])
    elif data[i] == ')':
        if stack[-1][0] == '(':
            tmp = stack.pop()
            result.append([tmp[1],i])
for i in range(1,len(result)+1):
    temp = list(itertools.combinations(result,i))
    for j in temp:
        result_data.append(j)
ans = []
for a in result_data:
    chk = []
    tmp = ""
    for b in a:
        chk.append(b[0])
        chk.append(b[1])
    for i in range(len(data)):
        if i not in chk:
            tmp += data[i]
    ans.append(tmp)
ans = list(set(ans))
ans = sorted(ans)
for res in ans:
    print(res)