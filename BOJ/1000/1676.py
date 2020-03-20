import sys
n = int(sys.stdin.readline())
fac = 1
for i in range(1,n+1):
    fac *= i
length = len(str(fac))
string = str(fac)
result = 0
for j in range(1,length+1):
    if string[-j] == '0':
        result+=1
    else:
        break
print(result)