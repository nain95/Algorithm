from itertools import permutations
import copy
def cul(oper,num,opers):
    cul_oper = copy.deepcopy(oper)
    cul_num = copy.deepcopy(num)
    for z in opers:
        op = z
        for j in range(len(cul_oper)):
            if cul_oper[j] == op:
                if op == '*':
                    for i in range(j+1,len(cul_num)):
                        if cul_num[i] != 'False':
                            cul_num[i] = cul_num[j] * cul_num[i]
                            cul_num[j] = 'False'
                            break
                if op == '-':
                    for i in range(j+1,len(cul_num)):
                        if cul_num[i] != 'False':
                            cul_num[i] = cul_num[j] - cul_num[i]
                            cul_num[j] = 'False'
                            break
                if op == '+':
                    for i in range(j+1,len(cul_num)):
                        if cul_num[i] != 'False':
                            cul_num[i] = cul_num[j] + cul_num[i]
                            cul_num[j] = 'False'
                            break
    return abs(cul_num[-1])

def solution(expression):
    answer_list = []
    oper = []
    num = []
    numstr = ''
    for i in range(len(expression)):
        if expression[i] == '*' or expression[i] == '-' or expression[i] == '+':
            oper.append(expression[i])
            num.append(int(numstr))
            numstr = ''
        else:
            numstr += expression[i]
    num.append(int(numstr))
    opers = list(permutations(list(set(oper)),len(list(set(oper)))))
    for o in opers:
        answer_list.append(cul(oper,num,o))
    answer = max(answer_list)
    return answer
#solution("100-200*300-500+20")
solution("1+0*2+100-20")
solution("1+0")