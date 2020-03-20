import sys,bisect
n,m = map(int,sys.stdin.readline().rstrip().split())
data = []
for _ in range(n):
    data.append(sys.stdin.readline().rstrip())
data.sort()
result = []
ans = 0
for _ in range(m):
    tmp = sys.stdin.readline().rstrip()
    index = bisect.bisect_left(data,tmp)
    if index < len(data):
        if data[index] == tmp:
            ans+=1
            result.append(tmp)
print(ans)
result.sort()
for i in result:
    print(i)