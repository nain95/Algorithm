import time
N,M = map(int,input().split())
#start = time.time()
queue = [[[N]]]
exit = True
cnt = 0
visited = [0]* 100001
while exit:
    nodes = queue.pop(0)
    tmp = []
    for node2 in nodes:
        for node in node2:
            if node > 100000:
                continue
            if visited[node] == 1:
                continue
            #print(node)
            visited[node] = 1
            x = node
            px = x+1
            sx = x-1
            mx = x*2
            if x == M:
                exit =False
                break
            if px == M or sx == M or mx == M:
                cnt+=1
                exit = False
                break
            temp = []
            if px > 0 :
                temp.append(px)
            if sx > 0:
                temp.append(sx)
            if mx > 0 :
                temp.append(mx)
            tmp.append(temp)
        if exit == False:
            break
    if tmp and exit ==True:
        cnt+=1
        queue.append(tmp)
print(cnt)
#print("time :", time.time() - start)