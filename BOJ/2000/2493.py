import sys
n = int(sys.stdin.readline())
towers = list(map(int,sys.stdin.readline().split()))
answer = [0]*n
stack = []
for ind,tower in enumerate(towers):
    while stack:
        if towers[stack[-1]]<tower:
            stack.pop()
        elif towers[stack[-1]]>tower:
            answer[ind] = stack[-1]+1
            break
    stack.append(ind)
for ans in answer:
    print(ans,end=' ')