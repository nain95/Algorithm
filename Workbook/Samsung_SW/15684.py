import sys,copy
def check():
    for i in range(1,N+1):
        cur = i
        for j in range(1,H+1):
            if data[j][cur]:
                cur += 1
            elif data[j][cur-1]:
                cur -= 1
        if cur != i:
            return False
    return True

def solve(cur):
    global min_result,data,exit
    if check():
        min_result = min(min_result,cur)
        if min_result == 0:
            print(0)
            sys.exit()
        elif min_result == 1:
            print(1)
            sys.exit()
        elif min_result == 2:
            exit = 2
        return
    if cur == exit:
        return
    for i in range(1,H+1):
        for j in range(1,N):
            if data[i][j] == 0 and data[i][j-1] == 0 and data[i][j+1] == 0:
                data[i][j] = 1
                solve(cur+1)
                data[i][j] = 0

N,M,H = map(int,sys.stdin.readline().split())
data = [[0]*(N+1) for _ in range(H+1)]
for _ in range(M):
    temp = list(map(int,sys.stdin.readline().split()))
    data[temp[0]][temp[1]] = 1
min_result = sys.maxsize
exit = 3
solve(0)
if min_result > 3:
    print(-1)
else:
    print(min_result)