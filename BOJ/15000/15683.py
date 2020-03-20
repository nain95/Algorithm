import sys,copy


def up(A):
    for i in range(A[0],-1,-1):
        if data[i][A[1]] == 6:
            break
        data[i][A[1]] = 7


def down(A):
    for i in range(A[0], N):
        if data[i][A[1]] == 6:
            break
        elif data[i][A[1]] == 0:
            data[i][A[1]] = 7


def left(A):
    for i in range(A[1],-1,-1):
        if data[A[0]][i] == 6:
            break
        elif data[A[0]][i] == 0:
            data[A[0]][i] = 7


def right(A):
    for i in range(A[1], M):
        if data[A[0]][i] == 6:
            break
        elif data[A[0]][i] == 0:
            data[A[0]][i] = 7

def solve(cur):
    global result,data
    original = copy.deepcopy(data)
    if cur == len(cctv):
        cnt = 0
        for i in data:
            cnt += i.count(0)

        result = min(result,cnt)
        if result == 0:
            print(0)
            sys.exit()
        return
    if data[cctv[cur][0]][cctv[cur][1]] == 1:
        for i in range(4):
            if i == 0:
                up(cctv[cur])
            elif i == 1:
                down(cctv[cur])
            elif i == 2:
                left(cctv[cur])
            elif i == 3:
                right(cctv[cur])
            solve(cur + 1)
            data = copy.deepcopy(original)
    elif data[cctv[cur][0]][cctv[cur][1]] == 2:
        for i in range(2):
            if i == 0:
                left(cctv[cur])
                right(cctv[cur])
            else:
                up(cctv[cur])
                down(cctv[cur])
            solve(cur + 1)
            data = copy.deepcopy(original)
    elif data[cctv[cur][0]][cctv[cur][1]] == 3:
        for i in range(4):
            if i == 0:
                up(cctv[cur])
                right(cctv[cur])
            elif i == 1:
                right(cctv[cur])
                down(cctv[cur])
            elif i == 2:
                down(cctv[cur])
                left(cctv[cur])
            elif i == 3:
                up(cctv[cur])
                left(cctv[cur])
            solve(cur + 1)
            data = copy.deepcopy(original)
    elif data[cctv[cur][0]][cctv[cur][1]] == 4:
        for i in range(4):
            if i == 0:
                up(cctv[cur])
                right(cctv[cur])
                left(cctv[cur])
            elif i == 1:
                right(cctv[cur])
                down(cctv[cur])
                left(cctv[cur])
            elif i == 2:
                up(cctv[cur])
                down(cctv[cur])
                left(cctv[cur])
            elif i == 3:
                up(cctv[cur])
                down(cctv[cur])
                right(cctv[cur])
            solve(cur + 1)
            data = copy.deepcopy(original)
    elif data[cctv[cur][0]][cctv[cur][1]] == 5:
        up(cctv[cur])
        down(cctv[cur])
        right(cctv[cur])
        left(cctv[cur])
        solve(cur+1)
        data = copy.deepcopy(original)


result = 100
N,M = map(int,sys.stdin.readline().split())
data = []
cctv = []
for i in range(N):
    temp = list(map(int,sys.stdin.readline().split()))
    data.append(temp)
    for j in range(M):
        if temp[j] != 0 and temp[j] != 6:
            cctv.append([i,j])
solve(0)
print(result)