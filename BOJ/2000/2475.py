import sys
data = list(map(int,sys.stdin.readline().split()))
result = 0
for i in data:
    result += pow(i,2)
print(result%10)