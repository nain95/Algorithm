def d(num):
    x = int(num / 1000);
    y = int(num % 1000 / 100);
    z = int(num % 100 / 10);
    w = int(num % 10);
    return num+x+y+z+w
temp_list= [0]*10000
for i in range(10000):
    d_num = d(i)
    if d_num<10000:
        temp_list[d_num] = 1
for j in range(10000):
    if temp_list[j] != 1:
        print(j)