import sys
from _collections import deque

def cal_max(A):
    max_return = 0
    for i in A:
        max_return = max(max_return, max(i))
    return max_return

def compare(A,B):
    for i in range(N):
        for j in range(N):
            if A[i][j] != B[i][j]:
                return True
    return False

def game(cur):
    global cube,max_num,caldata
    original = [x[:] for x in cube]
    if cal_max(cube) <= caldata[cur]:
        return
    if cur == 10:
        max_num = max(max_num, cal_max(cube))
        v = max_num
        while cur >= 0:
            caldata[cur] = v
            cur -= 1
            v//=2
        return
    for q in range(4):
        if q == 0:
            for i in range(len(cube)):
                temp = deque()
                check = 0
                for j in cube[i]:
                    if j == 0:
                        continue
                    if len(temp) == 0:
                        temp.append(j)
                    elif temp[-1] == j and check == 0:
                        temp[-1] *= 2
                        check = 1
                    else:
                        temp.append(j)
                        check = 0
                leng = len(temp)
                for z in range(leng):
                    cube[i][z] = temp.popleft()
                for z in range(leng, N):
                    cube[i][z] = 0
        elif q == 1:
            for i in range(len(cube)):
                temp = deque()
                check = 0
                for j in range(len(cube[i]) - 1, -1, -1):
                    if cube[i][j] == 0:
                        continue
                    if len(temp) == 0:
                        temp.append(cube[i][j])
                        continue
                    if temp[-1] == cube[i][j] and check == 0:
                        temp[-1] *= 2
                        check = 1
                    else:
                        temp.append(cube[i][j])
                        check = 0
                leng = len(temp)
                for z in range(N - leng):
                    cube[i][z] = 0
                for z in range(N - leng, N):
                    cube[i][z] = temp.pop()
        elif q == 2:
            for i in range(N):
                temp = deque()
                check = 0
                for j in range(N):
                    if cube[j][i] == 0:
                        continue
                    if len(temp) == 0:
                        temp.append(cube[j][i])
                    elif temp[-1] == cube[j][i] and check == 0:
                        temp[-1] *= 2
                        check = 1
                    else:
                        temp.append(cube[j][i])
                        check = 0
                leng = len(temp)
                for z in range(leng):
                    cube[z][i] = temp.popleft()
                for z in range(leng, N):
                    cube[z][i] = 0
        elif q == 3:
            for i in range(N):
                temp = deque()
                check = 0
                for j in range(N - 1, -1, -1):
                    if cube[j][i] == 0:
                        continue
                    if len(temp) == 0:
                        temp.append(cube[j][i])
                    elif temp[-1] == cube[j][i] and check == 0:
                        temp[-1] *= 2
                        check = 1
                    else:
                        temp.append(cube[j][i])
                        check = 0
                leng = len(temp)
                for z in range(N - 1, N - leng - 1, -1):
                    cube[z][i] = temp.popleft()
                for z in range(N - leng - 1, -1, -1):
                    cube[z][i] = 0
        flag = compare(original,cube)
        if flag:
            game(cur + 1)
            cube = [x[:] for x in original]
    return
N = int(sys.stdin.readline())
cube = []
test = 1
caldata = [0]*11
for _ in range(N):
    cube.append(list(map(int, sys.stdin.readline().split())))
max_num = 0
if N == 1:
    print(cube[0][0])
    sys.exit()
game(0)
print(max_num)
