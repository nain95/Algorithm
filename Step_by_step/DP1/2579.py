N = int(input())
stairs_list = [0]
zero_max = [0]
one_max = [0]
for _ in range(N):
    stairs = int(input())
    stairs_list.append(stairs)
for i in range(1,len(stairs_list)):
    if i == 1:
        zero_max.append(stairs_list[i])
        one_max.append(stairs_list[i])
    else:
        zero_max.append(max(zero_max[i-2],one_max[i-2])+stairs_list[i])
        one_max.append(zero_max[i-1]+stairs_list[i])
print(max(zero_max[-1],one_max[-1]))
