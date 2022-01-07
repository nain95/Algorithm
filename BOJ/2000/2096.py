import sys

n = int(sys.stdin.readline())
a, b, c = map(int,sys.stdin.readline().split())
max_value = [[a,b,c]]
min_value = [[a,b,c]]
for _ in range(n - 1):
    i = 0
    a, b, c = map(int,sys.stdin.readline().split())
    tmp_max_value = [a, b, c]
    tmp_min_value = [a, b, c]
    tmp_max_value[0] += max(max_value[i][0], max_value[i][1])
    tmp_max_value[1] += max(max_value[i])
    tmp_max_value[2] += max(max_value[i][1], max_value[i][2])

    tmp_min_value[0] += min(min_value[i][0], min_value[i][1])
    tmp_min_value[1] += min(min_value[i])
    tmp_min_value[2] += min(min_value[i][1], min_value[i][2])

    max_value.pop()
    min_value.pop()
    max_value.append(tmp_max_value)
    min_value.append(tmp_min_value)
print(max(max_value[-1]), end=' ')
print(min(min_value[-1]))