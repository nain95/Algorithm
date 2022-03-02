import sys
from turtle import left

n, s = map(int, sys.stdin.readline().split())
num_list = [i for i in list(map(int, sys.stdin.readline().split()))]
start = 0
ans = float('inf')
# sum_list = [0]
# for i in range(n):
#     sum_list.append(sum_list[i] + num_list[i])
# while end < (n+1):
#     if sum_list[end] - sum_list[start] >= s or end-start >= ans:
#         ans = min(ans, end-start)
#         start += 1
#         end = start
#     else:
#         end += 1
# if ans > 100000:
#     print(0)
# else:
#     print(ans)
sum_value = 0
for end in range(n):
    sum_value += num_list[end]
    while sum_value - num_list[start] >= s:
        sum_value -= num_list[start]
        start += 1
    if sum_value >= s and ans > end - start:
        ans = end - start + 1
print(ans if ans != float('inf') else 0)