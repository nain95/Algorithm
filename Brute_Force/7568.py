import sys
num = int(sys.stdin.readline().rstrip())
data = []
for i in range(num):
    temp_data = list(map(int,(sys.stdin.readline().rstrip()).split()))
    data.append(temp_data)
for j in range(len(data)):
    grade = 1
    for z in range(len(data)):
        if z == j:
            continue
        if data[j][0] < data[z][0] and data[j][1] < data[z][1]:
            grade += 1
    print(grade,end=" ")