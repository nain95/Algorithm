import sys
N = int(sys.stdin.readline())
num = list(map(int,sys.stdin.readline().split()))
result = 0
for i in num:
    if i == 1:
        continue
    chk = 0
    tmp = int(pow(i,0.5))+1
    for j in range(2,tmp):
        if i%j == 0:
            chk = 1
            break
    if chk == 0:
        result +=1
print(result)