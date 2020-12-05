t = int(input())
for case in range(t):
    n = int(input())
    data = input().split()
    x = 0
    print(f'#{case+1}',end=' ')
    if len(data) % 2 == 0:
        y = len(data)//2
        while y != len(data):
            print(f'{data[x]} {data[y]}',end=' ')
            x+=1
            y+=1
        print()
    else:
        y = len(data)//2+1
        while y != len(data):
            print(f'{data[x]} {data[y]}',end=' ')
            x+=1
            y+=1
        print(f'{data[x]}')