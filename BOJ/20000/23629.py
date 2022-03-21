import math
import sys

# sys.setrecursionlimit(10**6)
# string = input()
# str_to_num_dic = {"ZERO": "0", "ONE" : "1", "TWO" : "2", "THREE": "3", "FOUR" : "4", "FIVE" : "5", "SIX" : "6", "SEVEN" : "7", "EIGHT" : "8", "NINE" : "9", "x" : "*"}
# for s in str_to_num_dic:
#     string = string.replace(s, str_to_num_dic[s])
# tmp_string = ""
# flag = True
# ans = ""
# for idx, tmp in enumerate(string):
#     if tmp == '+' or tmp == '-' or tmp == '/' or tmp == '*':
#         tmp_string = "(" + tmp_string + ")"
#     tmp_string += tmp
#     try:
#         ans += str(math.trunc(eval(tmp_string[:-1])))
#     except:
#         print("Madness!")
# for s in str_to_num_dic:
#     ans = ans.replace(str_to_num_dic[s], s)
# print(string.replace("*", "x"))
# print(ans)


sys.setrecursionlimit(10**6)
string = input()
str_to_num_dic = {"ZERO": "0", "ONE" : "1", "TWO" : "2", "THREE": "3", "FOUR" : "4", "FIVE" : "5", "SIX" : "6", "SEVEN" : "7", "EIGHT" : "8", "NINE" : "9"}
for s in str_to_num_dic:
    string = string.replace(s, str_to_num_dic[s])
tmp_string = ""
flag = True
number = 0
ans = 0
cul = -1
for idx, tmp in enumerate(string):
    if idx != len(string)-1 and tmp == '=':
        print("Madness!")
        exit()
    if tmp.isalpha() and tmp != 'x':
        print("Madness!")
        exit()
    if (tmp == '+' or tmp == '-' or tmp == '/' or tmp == 'x' or tmp == '='):
        if not flag and number == 0:
            print("Madness!")
            exit()
        if cul != -1:
            if cul == 0:
                ans += number
            elif cul == 1:
                ans -= number
            elif cul == 2:
                ans *= number
            elif cul == 3:
                ans /= number
                ans = int(ans)
        if tmp == '+':
            cul = 0
        elif tmp == '-':
            cul = 1
        elif tmp == 'x':
            cul = 2
        elif tmp == '/':
            cul = 3
        flag = False
        number = 0
    elif flag:
        ans *= 10
        ans += int(tmp)
    else:
        number *= 10
        number += int(tmp)
ans = str(ans)
for s in str_to_num_dic:
    ans = ans.replace(str_to_num_dic[s], s)
print(string)
print(ans)
