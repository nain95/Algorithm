import sys
data = {}
for i in range(8):
    data[int(sys.stdin.readline())] = i+1
sort_data = sorted(data)
print(sum(sort_data[3:]))
result = []
for j in range(3,8):
    result.append(data[sort_data[j]])
for i in sorted(result):
    print(i,end = ' ')