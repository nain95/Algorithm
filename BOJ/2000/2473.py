# import sys

# n = int(sys.stdin.readline())
# input_data = sorted(list(map(int, sys.stdin.readline().split())))
# left, right = 0, n-1
# min_sum = float('inf')
# ans_left, ans_right, ans_middle = left, right, (left + right) // 2
# for left in range(n-2):
#     for right in range(left + 2, n):
#         tmp_left, tmp_right, tmp_middle = left + 1, right - 1, (left + right) // 2
#         tmp_min_sum = min_sum
#         while tmp_left <= tmp_right:
#             middle = (tmp_left + tmp_right) // 2
#             if abs(tmp_min_sum) > abs(input_data[left] + input_data[right] + input_data[middle]):
#                 tmp_min_sum = input_data[left] + input_data[right] + input_data[middle]
#                 tmp_middle = middle
#             if input_data[left] + input_data[right] + input_data[middle] < 0:
#                 tmp_left = middle + 1
#             else:
#                 tmp_right = middle - 1
#         if abs(min_sum) > abs(tmp_min_sum):
#             min_sum = tmp_min_sum
#             ans_left, ans_right, ans_middle = left, right, tmp_middle
# print(input_data[ans_left], input_data[ans_middle] ,input_data[ans_right])

import sys

n = int(sys.stdin.readline())
input_data = sorted(list(map(int, sys.stdin.readline().split())))
sum_data = float('inf')
for i in range(n-2):
    left, right = i+1, n-1
    while left < right:
        tmp_sum = input_data[i] + input_data[left] + input_data[right]
        if abs(sum_data) > abs(tmp_sum):
            sum_data = tmp_sum
            ans_i, ans_left, ans_right = i, left, right
        if tmp_sum < 0:
            left += 1
        elif tmp_sum > 0:
            right -= 1
        else:
            print(input_data[ans_i], input_data[ans_left], input_data[ans_right])
            exit()
print(input_data[ans_i], input_data[ans_left], input_data[ans_right])