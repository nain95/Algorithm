import sys
from collections import deque


def bfs():
    queue = deque([1])
    depth = 0
    visited = [0] * 101
    while queue:
        length = len(queue)
        for _ in range(length):
            cur = queue.popleft()
            visited[cur] = 1
            if cur == 100:
                return depth
            for i in range(1, 7):
                if cur + i > 100:
                    break
                if visited[cur + i] == 0:
                    if cur + i in dic_ladder:
                        if visited[dic_ladder[cur + i]] == 0:
                            queue.append(dic_ladder[cur + i])
                    elif cur + i in dic_snake:
                        if visited[dic_snake[cur + i]] == 0:
                            queue.append(dic_snake[cur + i])
                    else:
                        queue.append(cur + i)
        depth += 1


if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().split())
    dic_ladder = {}
    dic_snake = {}
    for _ in range(n):
        start, end = map(int, sys.stdin.readline().split())
        dic_ladder[start] = end
    for _ in range(m):
        start, end = map(int, sys.stdin.readline().split())
        dic_snake[start] = end
    print(bfs())