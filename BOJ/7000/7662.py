import sys, heapq, copy
from _collections import defaultdict

T = int(sys.stdin.readline())
for _ in range(T):
    k = int(sys.stdin.readline())
    min_heap = []
    max_heap = []
    min_dic = defaultdict(int)
    max_dic = defaultdict(int)
    for _ in range(k):
        command, num = list(sys.stdin.readline().split())
        num = int(num)
        if command == 'I':
            heapq.heappush(min_heap, num)
            heapq.heappush(max_heap, [-num, num])
        else:
            chk = True
            if num == -1:
                while chk:
                    if min_heap:
                        item = heapq.heappop(min_heap)
                        if max_dic[item]:
                            max_dic[item] -= 1
                        else:
                            chk = False
                            min_dic[item] += 1
                    else:
                        chk = False
            else:
                while chk:
                    if max_heap:
                        _, item = heapq.heappop(max_heap)
                        if min_dic[item]:
                            min_dic[item] -= 1
                        else:
                            chk = False
                            max_dic[item] += 1
                    else:
                        chk = False

    answer_min, answer_max = -1, -1

    if not min_heap:
        print('EMPTY')
        continue

    while max_heap and min_dic[max_heap[0][1]]:
        _, i = heapq.heappop(max_heap)
        min_dic[i] -= 1

    if not max_heap:
        print('EMPTY')
        continue

    while min_heap and max_dic[min_heap[0]]:
        i = heapq.heappop(min_heap)
        max_dic[i] -= 1

    print(max_heap[0][1], min_heap[0])