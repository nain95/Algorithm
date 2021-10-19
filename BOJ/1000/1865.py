import sys
from collections import defaultdict

def bellman_ford(start : int, v : int) -> bool:
    distance[start][start] = 0
    for _ in range(n):
        for node in range(1, n + 1):
            for end, time in road[node].items():
                distance[start][end] = min(distance[start][node] + time, distance[start][end])
    for node in range(1, n + 1):
        for end, time in road[node].items():
            if distance[start][end] > distance[start][node] + time:
                return False
    return True

def solve() -> str:
    for x in range(1, n + 1):
        for y in range(1, n + 1):
            if distance[x][y] + distance[y][x] < 0:
                return 'YES'
    return 'NO'

if __name__=='__main__':
    n = int(sys.stdin.readline())
    for _ in range(n):
        n, m, w = map(int, sys.stdin.readline().split())
        distance = [[2000000000] * (n + 1) for _ in range(n + 1)]
        v = (2 * m) + w
        road = defaultdict(dict)
        for _ in range(m):
            s, e, t = map(int, sys.stdin.readline().split())
            if e in road[s]:
                road[s][e] = min(road[s][e], t)
                road[e][s] = min(road[e][s], t)
            else:
                road[s][e] = t
                road[e][s] = t
        for _ in range(w):
            s, e, t = map(int, sys.stdin.readline().split())
            road[s][e] = -t
        if bellman_ford(1, v) == False:
            print('YES')
        else:
            print('NO')
            