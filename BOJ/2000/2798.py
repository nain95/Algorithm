import itertools
import sys
num = list(map(int,(sys.stdin.readline().rstrip()).split()))
data_list = list(map(int,(sys.stdin.readline().rstrip()).split()))
com_list = list(itertools.combinations(data_list,3))
result = 0
for i in com_list:
    sum = i[0]+i[1]+i[2]
    if sum <= num[1] and result < sum:
        result = sum
print(result)