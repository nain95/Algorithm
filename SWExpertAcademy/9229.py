t = int(input())
for case in range(t):
    n, m = map(int,input().split())
    snack = list(map(int,input().split()))
    snack = sorted(snack)
    result = -1
    for i in range(n-1):
        for j in range(n-1,i,-1):
            if snack[j] > m:
                continue
            if snack[i] + snack[j] > m:
                continue
            if snack[i] +snack[j] <= result:
                break
            else:
                result = max(result,snack[i]+snack[j])
    print(result)