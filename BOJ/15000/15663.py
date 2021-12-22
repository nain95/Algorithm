import sys


def permutation(arr, r, chosen, used):
    global pre_list
    if len(chosen) == r:
        for n in chosen:
            print(n, end=" ")
        print()
        return
    tmp = -1
    for i in range(len(arr)):
        if tmp != arr[i] and (
            (not used[i] and not chosen)
            or (not used[i] and chosen and chosen[-1] <= arr[i])
        ):
            chosen.append(arr[i])
            used[i] = 1
            tmp = arr[i]
            permutation(arr, r, chosen, used)
            used[i] = 0
            chosen.pop()


n, m = map(int, sys.stdin.readline().split())
num_list = list(map(int, sys.stdin.readline().split()))
num_list = num_list * m
pre_list = []
permutation(sorted(num_list), m, [], [0 for _ in range(len(num_list))])
"""for num in permutation(sorted(num_list), m, [], [0 for _ in range(len(num_list))], []):
    print(num)
    if tmp == [] or tmp != num:
        for i in num:
            print(i, end=" ")
        print()
    else:
        continue"""
