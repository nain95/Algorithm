import sys
N = list(map(int,list(sys.stdin.readline().rstrip())))
sort_N = sorted(N)
result = 0
for i in range(len(N)-1,-1,-1):
    result += sort_N[i]*pow(10,i)
print(result)