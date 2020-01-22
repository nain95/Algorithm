import sys
N = int(sys.stdin.readline().rstrip())
stack = []
for _ in range(N):
    tmp = int(sys.stdin.readline().rstrip())
    if tmp == 0:
        stack.pop()
    else:
        stack.append(tmp)
print(sum(stack))