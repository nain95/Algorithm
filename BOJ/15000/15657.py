import sys
def combinations_2(array, r):
    for i in range(len(array)):
        if r == 1:
            yield [array[i]]
        else:
            for next in combinations_2(array[i:], r-1):
                yield [array[i]] + next

n, m = map(int, sys.stdin.readline().split())
num_list = list(map(int, sys.stdin.readline().split()))
num_list.sort()
for i in combinations_2(num_list,m):
    for ans in i:
        print(ans, end=' ')
    print()
