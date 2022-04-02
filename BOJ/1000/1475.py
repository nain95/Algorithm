import math

num = int(input())
num_list = [0] * 10
if num == 0:
    print(1)
else:
    while num:
        tmp = num % 10
        if tmp == 9:
            tmp = 6
        num_list[tmp] += 1
        num //= 10
    num_list[6] = math.ceil(num_list[6] / 2)
    print(max(num_list))
