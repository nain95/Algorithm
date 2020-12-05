for case in range(1,11):
    n = int(input())
    cnt = 0
    result = 1
    for _ in range(n):
        data = input().split()
        if len(data) == 4 and data[1].isdecimal():
            result = 0
        if data[1].isdecimal():
            cnt += 1
        else:
            cnt -= 1
    if cnt != 1:
        result = 0
    print(f'#{case} {result}')