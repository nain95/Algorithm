import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
queue = deque([n])
func = [[lambda x: x - 1, 1], [lambda x: x + 1, 1], [lambda x: x * 2, 1]]
distance = [float("INF")] * 1000000
distance[n] = 0
move = 0
a_visited = [-1] * 1000000
a_visited[n] = 1
b_visited = [-1] * 1000000
while queue:
    length = len(queue)
    for _ in range(length):
        cur = queue.popleft()
        if move % 2 == 0 and a_visited[k] == 1:
            break
        elif move % 2 == 1 and b_visited[k] == 1:
            break
        if cur == k:
            break
        for f, weight in func:
            if 0 <= f(cur) <= 500000:
                if (move+1) % 2 == 0 and a_visited[f(cur)] == -1:
                    queue.append(f(cur))
                    distance[f(cur)] = distance[cur] + weight
                    a_visited[f(cur)] = 1
                elif (move+1) % 2 == 1 and b_visited[f(cur)] == -1:
                    queue.append(f(cur))
                    distance[f(cur)] = distance[cur] + weight
                    b_visited[f(cur)] = 1
    else:
        move += 1
        k += move
        if k > 500000:
            print(-1)
            exit()
        continue
    break
print(move if distance[k] != float('inf') else -1)
