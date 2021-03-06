import sys,heapq
V,E = map(int,sys.stdin.readline().split())
K = int(sys.stdin.readline())
heap = []
dist = [V*11]*(V+1)
adj = [[V*11]*(V+1) for _ in range(V+1)]
dist[K] = 0
for _ in range(E):
    temp = list(map(int,sys.stdin.readline().split()))
    adj[temp[0]][temp[1]] = temp[2]
for i in range(1,V+1):
    if i == K:
        heapq.heappush(heap,(0,i))
    else:
        heapq.heappush(heap, (V*11, i))
while 1:
    if heap == []:
        break
    if heap[0][1] == V*11:
        break
    pop_data = heapq.heappop(heap)
    if pop_data[0] > dist[pop_data[1]]:
        continue
    else:
        for i in range(len(adj[pop_data[1]])):
            if adj[pop_data[1]][i] != V*11:
                dist[i] = min(dist[i],dist[pop_data[1]]+adj[pop_data[1]][i])
                heapq.heappush(heap,(dist[i],i))
for i in range(1,len(dist)):
    if dist[i] == V*11:
        print('INF')
    else:
        print(dist[i])