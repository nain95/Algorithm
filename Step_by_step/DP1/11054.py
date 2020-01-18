N = int(input())
data = list(map(int,input().split()))
list1 = [1]+[0]*(N-1)
list2 = [0]*(N-1)+[1]
for i in range(1,len(data)):
    max_data1 = 0
    for j in range(i):
        if max_data1 < list1[j] and data[j] < data[i]:
            max_data1 = list1[j]
    list1[i] = max_data1 +1
for z in range(len(data)-1,-1,-1):
    max_data = 0
    for y in range(z,len(data)):
        if max_data < list2[y] and data[y] < data[z]:
            max_data = list2[y]
    list2[z] = max_data +1
temp = []
for i in range(N):
    temp.append(list1[i]+list2[i])
result = max(temp)-1
if result == 0:
    print(1)
else:
    print(result)