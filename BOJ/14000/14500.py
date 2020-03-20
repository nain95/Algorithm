import sys
def sum(A):
    sum_data=0
    for i in A:
        sum_data+=i
    return sum_data
N,M = map(int,sys.stdin.readline().split())
data = []
max_data = 0
for _ in range(N):
    data.append(list(map(int,sys.stdin.readline().split())))
    max_data = max(max_data,max(data[-1]))
max_data *= 4
cal_max = 0
def first():
    global cal_max
    for i in range(N):
        for j in range(0,M-3):
            if max_data == sum(data[i][j:j + 4]):
                print(max_data)
                sys.exit()
            cal_max = max(cal_max,sum(data[i][j:j+4]))
    for j in range(N-3):
        for i in range(0,M):
            sum_num = 0
            for z in range(j,j+4):
                sum_num += data[z][i]
            if sum_num == max_data:
                print(max_data)
                sys.exit()
            cal_max = max(cal_max, sum_num)
def second():
    global cal_max
    for i in range(N-1):
        for j in range(0,M-1):
            cal = sum(data[i+1][j:j + 2])+data[i][j]
            temp = []
            if i!= 0:
                temp.append(data[i-1][j])
            if j!= 0:
                temp.append(data[i][j-1])
                temp.append(data[i+1][j-1])
            if i!= N-2:
                temp.append(data[i+2][j])
                temp.append(data[i+2][j+1])
            if j != M-2:
                temp.append(data[i+1][j+2])
            temp.append(data[i][j+1])
            cal += max(temp)
            cal_max = max(cal_max,cal)

            cal = sum(data[i][j:j + 2]) + data[i+1][j]
            temp = []
            if i!= 0:
                temp.append(data[i-1][j+1])
            if j != 0:
                temp.append(data[i][j - 1])
                temp.append(data[i + 1][j - 1])
            if i != N - 2:
                temp.append(data[i + 2][j])
            if j != M - 2:
                temp.append(data[i][j + 2])
            cal += max(temp)
            cal_max = max(cal_max, cal)

            cal = sum(data[i][j:j + 2]) + data[i + 1][j+1]
            temp = []
            if i != 0:
                temp.append(data[i - 1][j + 1])
            if j != 0:
                temp.append(data[i][j - 1])
            if i != N - 2:
                temp.append(data[i + 2][j+1])
            cal += max(temp)
            cal_max = max(cal_max, cal)

            cal = sum(data[i+1][j:j + 2]) + data[i][j + 1]
            temp = []
            if i != 0:
                temp.append(data[i - 1][j + 1])
            if j != 0:
                temp.append(data[i+1][j - 1])
            if i != N - 2:
                temp.append(data[i + 2][j])
            cal += max(temp)
            cal_max = max(cal_max, cal)
first()
second()
print(cal_max)