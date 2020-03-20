import sys
input_data = sys.stdin.readline().rstrip()
count = 0
num = [[] for _ in range(100)]
tmp = ''
str_num = ''
check = 0
numcnt = 0
for i in range(len(input_data)):
    if i == len(input_data) - 1 and check == 1:
        str_num += input_data[i]
        tmp += str(int(str_num)) + ')'
        str_num = ''
    elif input_data[i].isdigit() and i == len(input_data)-1:
        str_num+=input_data[i]
        tmp += str(int(str_num))
    elif input_data[i].isdigit():
        str_num+=input_data[i]
    elif input_data[i] == '-' and check == 0:
        tmp+=str(int(str_num))+'-('
        check =1
        str_num=''
    elif input_data[i] == '-' and check == 1:
        tmp+=str(int(str_num))+')-('
        str_num = ''
    elif input_data[i] == '+':
        tmp+=str(int(str_num))+'+'
        str_num = ''

#print(tmp)
print(eval(tmp))