import sys

def gcd(a,b):
    while(b != 0):
        if(a<b):
            (a,b)=(b,a)
        temp=a%b
        a=b
        b=temp
    return a


n = int(sys.stdin.readline())
data = []
diff = []
for _ in range(n):
    data.append(int(sys.stdin.readline()))
data = sorted(data)
for i in range(n-1):
    diff.append(data[i+1]-data[i])
while len(diff) != 1:
    temp = []
    for i in range(len(diff)-1):
        temp.append(gcd(diff[i],diff[i+1]))
    diff = temp.copy()
dif = diff[0]
result = []
for i in range(1, int(dif**0.5)+1):
        if dif%i == 0:
            result.append(i)
            if i!=n//i:
                result.append(dif//i)
result = sorted(list(set(result)))
for i in result:
    if i == 1:
        continue
    print(i,end=' ')
