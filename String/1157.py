import sys
input_list = list(sys.stdin.readline().rstrip().upper())
set_list = list(set(input_list))
max = set_list[0]
max_count = input_list.count(set_list[0])
if len(set_list) == 1:
    print(max)
else:
    second_count = 0
    for i in range(1,len(set_list)):
        if max_count >= input_list.count(set_list[i]) and second_count < input_list.count(set_list[i]):
            second_count = input_list.count(set_list[i])
            second = set_list[i]
        elif max_count<input_list.count(set_list[i]):
            max = set_list[i]
            max_count = input_list.count(set_list[i])
    if max_count == second_count:
        print("?")
    else:
        print(max)