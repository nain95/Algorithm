import sys
n = int(sys.stdin.readline())
data = list(map(int,sys.stdin.readline().split()))
sorted_data = (sorted(list(set(data))))
dic = {}
for i in range(len(sorted_data)):
    dic[sorted_data[i]] = i
for j in data:
    print(dic[j],end=' ')