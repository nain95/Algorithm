import sys,copy
T = int(sys.stdin.readline())
for _ in range(T):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    data = []
    for j in range(n):
        data.append(j+1)
    if k == 0:
        print(n)
        continue
    for _ in range(k):
        new_data = []
        for i in range(len(data)):
            new_data.append(sum(data[:i+1]))
        data = copy.deepcopy(new_data)
    print(data[-1])