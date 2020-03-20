N = int(input())
for _ in range(N):
    data = [1, 2, 4]
    num = int(input())
    if num >3:
        for i in range(3,num):
            data.append(data[i-1]+data[i-2]+data[i-3])
    print(data[num-1])