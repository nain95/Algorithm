import sys
def min_max(num,num_list):
    min = num_list[0]
    max = num_list[0]
    for i in range(1,num):
        if num_list[i] < min:
            min = num_list[i]
        if num_list[i] > max:
            max = num_list[i]
    print(str(min) + " " + str(max))

num = int(sys.stdin.readline().rstrip())
num_list = list(map(int,(sys.stdin.readline().rstrip()).split()))
min_max(num,num_list)