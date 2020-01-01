def sum(N):
    str_num = str(N)
    for i in str_num:
        N+=int(i)
    return N

num =int(input())
for i in range(num):
    temp = sum(i)
    if temp == num:
        print(i)
        break
    if i == num-1:
        print(0)