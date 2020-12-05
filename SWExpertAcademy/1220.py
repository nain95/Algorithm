for case in range(1,11):
    n = int(input())
    table = [[int(x) for x in input().split()] for _ in range(n)]
    result = 0
    for i in range(n):
        chk = False
        for j in range(n):
            if table[j][i] == 1:
                chk = True
            elif table[j][i] == 2 and chk:
                result += 1
                chk = False
    print(f'#{case} {result}')

