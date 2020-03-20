import sys
N = int(sys.stdin.readline().rstrip())
data = []
check = [0]*8001
for _ in range(N):
    tmp = int(sys.stdin.readline().rstrip())
    data.append(tmp)
    check[tmp+4000]+=1
sort_data = sorted(data)
max = 1
num = []
for i in range(len(check)):
    if check != 0:
        if max < check[i]:
            num = [i-4000]
            max = check[i]
        elif max == check[i]:
            num.append(i-4000)
print('%d'%round(sum(data)/N*1.0))
print('%d'%sort_data[N//2])
if len(num) == 1:
    print(num[0])
else:
    print(num[1])
print('%d'%(sort_data[-1]-sort_data[0]))