import sys

for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    choice = [-1] + [i for i in map(int,sys.stdin.readline().split())]
    visited = [0] * (n + 1)
    ans = []
    for idx in range(1, n + 1):
        if visited[idx]:
            continue
        stack = [idx]
        cycle = []
        while stack:
            cur = stack.pop()
            visited[cur] = 1
            cycle.append(cur)
            stack.append(choice[cur])
            if visited[choice[cur]]: 
                if choice[cur] in cycle:
                    ans += cycle[cycle.index(choice[cur]):]
                break
    print(n - len(ans))