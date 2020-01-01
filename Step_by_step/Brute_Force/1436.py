result = []
num = int(input())
for i in range(2700000):
    str_i = str(i)
    for j in range(len(str_i)-2):
        if str_i[j]=='6' and str_i[j+1]=='6' and str_i[j+2] =='6':
            result.append(i)
            break
    if len(result) >= num:
        break
print(result[num-1])