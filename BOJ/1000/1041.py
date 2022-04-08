import sys

n = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
tmp = [[1,2], [1,3], [2,4], [3,4]]
sum_num = [min(num)]
sum_num.append(float('inf'))
if n == 1:
    print(sum(num) - max(num))
else:
    for a,b in tmp:
        sum_num[1] = min(sum_num[1], num[a] + num[b])
    for t in range(1, 5):
        z = min(num[0], num[5]) + num[t]
        sum_num[1] = min(sum_num[1], z)
    sum_num.append(float('inf'))
    for a,b in tmp:
        sum_num[2] = min(sum_num[2], min(num[0], num[5]) + num[a] + num[b])
    answer = sum_num[2] * 4 + sum_num[1] * max(0,(n-2)) * 8 + sum_num[0] * max(0, (n-2)) * (n-2) * 5 + sum_num[0] * max(0,(n-2)) * 4 + sum_num[1] * 4
    print(answer)
