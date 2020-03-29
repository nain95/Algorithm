import sys
r,c = map(int,sys.stdin.readline().split())
data = []
visit = [[0]*c for _ in range(r)]
for _ in range(r):
    data.append(list(map(int,sys.stdin.readline().split())))
result = []
if r % 2 == 1:
    for i in range(r):
        if i % 2 == 0:
            for _ in range(c-1):
                result.append('R')
            if i!= r-1:
                result.append('D')
        else:
            for _ in range(c-1):
                result.append('L')
            result.append('D')
elif c % 2 == 1:
    for i in range(c):
        if i % 2 == 0:
            for _ in range(r - 1):
                result.append('D')
            if i != c - 1:
                result.append('R')
        else:
            for _ in range(r - 1):
                result.append('U')
            result.append('R')
else:
    mindata = data[0][1]
    minindex = [0,1]
    for i in range(r):
        if i % 2 == 0:
            s = 1
        else:
            s = 0
        for j in range(s,c,2):
            if data[i][j] < mindata:
                mindata = data[i][j]
                minindex = [i,j]
    x,y = minindex
    resultA = []
    resultB = []
    x1 = 0
    y1 = 0
    x2 = r-1
    y2 = c-1
    while x2-x1 >1:
        if x1//2 < x//2:
            for _ in range(c-1):
                resultA.append('R')
            resultA.append('D')
            for _ in range(c-1):
                resultA.append('L')
            resultA.append('D')
            x1 += 2
        if x//2 < x2//2:
            for _ in range(c-1):
                resultB.append('R')
            resultB.append('D')
            for _ in range(c-1):
                resultB.append('L')
            resultB.append('D')
            x2 -= 2
    while y2 - y1 > 1:
        if y1 // 2 < y // 2 :
            resultA.append('D')
            resultA.append('R')
            resultA.append('U')
            resultA.append('R')
            y1 += 2

        if y // 2 < y2 // 2 :
            resultB.append('D')
            resultB.append('R')
            resultB.append('U')
            resultB.append('R')
            y2 -= 2

    if y == y1:
        resultA.append('R')
        resultA.append('D')
    else:
        resultA.append('D')
        resultA.append('R')

    resultB.reverse()
    result = resultA
    for a in resultB:
        result.append(a)

for ans in result:
    print(ans,end='')
