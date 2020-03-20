import sys
n,k = map(int,sys.stdin.readline().split())
data = []
for _ in range(n):
    temp = list(map(int,sys.stdin.readline().split()))
    data.append(temp[1:]+[temp[0]])
data = sorted(data)
for i in range(n):
    if data[i][3] == k:
        if i != n-1:
            for j in range(i,n):
                if data[j][:3] == data[j+1][:3]:
                    i+=1
                else:
                    break
        print(n-i)