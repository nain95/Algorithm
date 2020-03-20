import sys
for line in sys.stdin:
    n,k=map(int,line.split())
    result = n
    tmp = n
    if n==1 and k ==1:
        print(1)
        continue
    while 1:
        etc = tmp % k
        tmp = tmp//k
        result+=tmp
        tmp += etc
        if tmp < k:
            break
        elif tmp == k:
            result+=1
            break

    print(result)