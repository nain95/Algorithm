import sys
import bisect
from collections import defaultdict

def solution(a_list: list, b_list: list, k: int):
    answer = 0
    a_sum_list = []
    b_sum_list = []
    for data, sum_list in [[a_list, a_sum_list],[b_list, b_sum_list]]:
        for idx, num in enumerate(data):
            if not sum_list:
                sum_list.append(num)
            else:
                tmp_list = [num]
                for i in range(1, idx + 1):
                    tmp_list.append(sum_list[-i] + num)
                sum_list += tmp_list
    b_sum_list = sorted(b_sum_list)
    a_dic = defaultdict(int)
    for a in a_sum_list:
        a_dic[a] += 1
    for a in set(a_sum_list):
        idx = bisect.bisect_left(b_sum_list, k - a)
        while len(b_sum_list) > idx and b_sum_list[idx] == k - a:
            answer += a_dic[a]
            idx += 1
    print(answer)

if __name__ == '__main__':
    k = int(sys.stdin.readline())
    data_len = []
    input_data = []
    for _ in range(2):
        data_len.append(int(sys.stdin.readline()))
        input_data.append(list(map(int, sys.stdin.readline().split())))
    solution(input_data[0], input_data[1], k)

