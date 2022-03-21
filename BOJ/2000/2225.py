n, k = map(int, input().split())
dp = [1 if i <= n else 0 for i in range(k + 1)]
for i in range(2, n + 1):
    for j in range(k + 1):



        0 1 2 3 4 5 
     1  1 1 1 1 1 1
     2  1 2 3 4 5 6
     3  1 3 6 7