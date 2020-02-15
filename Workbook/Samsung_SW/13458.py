import sys
N = int(sys.stdin.readline())
cnt = list(map(int,sys.stdin.readline().split()))
B,C = map(int, sys.stdin.readline().split())
result = 0
for i in cnt:
    if i < B:
        result+=1
    else:
        cal = (i - B) % C
        if cal == 0:
            result+=1+((i - B) //C)
        else:
            result+=2+((i - B) //C)
print(result)