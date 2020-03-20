import sys
N = int(sys.stdin.readline().rstrip())
conference_input = []
for _ in range(N):
    conference_input.append(list(map(int,sys.stdin.readline().rstrip().split())))
cnt = 0
sorted_list = sorted(conference_input, key = lambda x : (x[1],x[0]))

start_time = -1
for i in range(N):
    if sorted_list[i][0] >= start_time:
        cnt = cnt + 1
        start_time = sorted_list[i][1]
print(cnt)
