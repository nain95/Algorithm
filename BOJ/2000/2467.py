import sys

n = int(sys.stdin.readline())
input_data = list(map(int, sys.stdin.readline().split()))
left, right = 0, n-1
sum_data = input_data[left] + input_data[right]
ans_left, ans_right = left, right
while left < right:
    tmp_sum = input_data[left] + input_data[right]
    if abs(sum_data) > abs(tmp_sum):
        sum_data = tmp_sum
        ans_left, ans_right = left, right
    if tmp_sum < 0:
        left += 1
    else:
        right -= 1
print(input_data[ans_left], input_data[ans_right])
