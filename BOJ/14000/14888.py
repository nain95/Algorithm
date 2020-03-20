import sys
import math
num = int(sys.stdin.readline().rstrip())
num_factorial = math.factorial(num-1)
num_list = list(map(int,sys.stdin.readline().rstrip().split()))
operator_num = list(map(int,sys.stdin.readline().rstrip().split()))
tmp=1
for i in operator_num:
    tmp*=math.factorial(i)
result = []
operator = []
exit = 0
def solution(cur):
    global exit,tmp
    if cur == num-1:
        exit+=1
        cur = 0
        temp = num_list[0]
        for i in range(1,len(num_list)):
            if operator[i-1] == 0:
                temp+=num_list[i]
            elif operator[i-1] == 1:
                temp-=num_list[i]
            elif operator[i-1] == 2:
                temp*=num_list[i]
            elif operator[i-1] == 3:
                if temp < 0 :
                    temp = -temp
                    temp//=num_list[i]
                    temp = -temp
                else:
                    temp//=num_list[i]
        result.append(temp)
        if exit == num_factorial//tmp:
            print(max(result))
            print(min(result))
            sys.exit()
    for i in range(4):
        if operator.count(i) >= operator_num[i]:
            continue
        operator.append(i)
        solution(cur+1)
        operator.pop()
solution(0)