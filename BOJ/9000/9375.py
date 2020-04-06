import sys
t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    clothes = {}
    for _ in range(n):
        name,type = sys.stdin.readline().rstrip().split()
        if type not in clothes:
            clothes[type] = 1
        else:
            clothes[type] += 1
    result = 1
    for i in clothes.values():
        result *= i+1
    print(result-1)
