import sys, heapq

def dijkstra(start, dis, flag):
    heap = []
    dis[start] = 0
    heapq.heappush(heap, [0, start])
    visited = [0] * (n + 1)
    if flag == 1:
        while heap:
            cur = heapq.heappop(heap)[1]
            visited[cur] = 1
            for i in range(1, n + 1):
                if visited[i] == 0 and distance[cur][i] != float('inf'): 
                    if dis[cur] + distance[cur][i] <= dis[i]:
                        dis[i] = dis[cur] + distance[cur][i]
                        heapq.heappush(heap, [dis[i], i])
    else:
        while heap:
            cur = heapq.heappop(heap)[1]
            visited[cur] = 1
            for i in range(1, n + 1):
                if visited[i] == 0 and distance[i][cur] != float('inf'):
                    if dis[cur] + distance[i][cur] <= dis[i]:
                        dis[i] = dis[cur] + distance[i][cur]
                        heapq.heappush(heap, [dis[i], i])
    return dis

n, m, x = map(int, sys.stdin.readline().split())
distance = [[float('inf')] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    start, end, time = map(int, sys.stdin.readline().split())
    distance[start][end] = time
a = dijkstra(x, distance[x][:], 1)
b = dijkstra(x, [distance[i][x] for i in range(n + 1)], 0)

print(max([a[i] + b[i] for i in range(1, len(distance[x]))]))
