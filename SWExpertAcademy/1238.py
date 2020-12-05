from _collections import deque

ls = input()
while ls:
    l,s = map(int,ls.split())
    data = list(map(int,input().split()))
    dic = {}
    max_num = 0
    called = [0] * 101
    waiting = deque([s])
    for i in range(0,len(data),2):
        fro,to = data[i],data[i+1]
        if fro in dic:
            dic[fro] = list(set(dic[fro]+[to]))
        else:
            dic[fro] = [to]
    last = []
    while waiting:
        len_waiting = len(waiting)
        last.append([])
        for _ in range(len_waiting):
            cur = waiting.popleft()
            if cur in dic:
                for c in dic[cur]:
                    if not called[c]:
                        called[c] = 1
                        waiting.append(c)
                        last[-1].append(c)
    print(max(last[-2]))
