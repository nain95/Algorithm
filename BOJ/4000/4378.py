import sys
line0 = ['`','1','2','3','4','5','6','7','8','9','0','-','=']
line1 = ['Q','W','E','R','T','Y','U','I','O','P','[',']','\\']
line2 = ['A','S','D','F','G','H','J','K','L',';','\'']
line3 = ['Z','X','C','V','B','N','M',',','.','/']

while(1):
    data = list(sys.stdin.readline().rstrip())
    if data == []:
        break
    for i in data:
        if i == ' ':
            print(' ',end = '')
        elif i in line0:
            print(line0[line0.index(i) - 1], end='')
        elif i in line1:
            print(line1[line1.index(i)-1],end = '')
        elif i in line2:
            print(line2[line2.index(i)-1],end = '')
        elif i in line3:
            print(line3[line3.index(i)-1],end = '')
    print()
