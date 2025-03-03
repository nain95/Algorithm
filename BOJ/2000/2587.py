num_list = []
for _ in range(5):
    num = int(input())
    num_list.append(num)
print(sum(num_list)//5)
print(sorted(num_list)[2])
