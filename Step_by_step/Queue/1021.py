import sys
from _collections import deque
N,M= map(int,sys.stdin.readline().rstrip().split())
input_data = deque(list(map(int,sys.stdin.readline().rstrip().split())))
queue = deque()
for i in range(1,N+1):
    queue.append(i)
result = 0
while input_data:
    if queue[0] == input_data[0]:
        queue.popleft()
        input_data.popleft()
    else:
        for j in range(len(queue)):
            if queue[j] == input_data[0]:
                break
        if j > (len(queue) // 2):
            for i in range(len(queue)-j):
                queue.appendleft(queue.pop())
                result+=1
        else:
            for i in range(j):
                queue.append(queue.popleft())
                result+=1
print(result)