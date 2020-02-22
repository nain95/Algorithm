import sys
def spin_left(A):
    tmp = A[0]
    for i in range(7):
        A[i] = A[i+1]
    A[7] = tmp
    return A
def spin_right(A):
    tmp = A[-1]
    for i in range(7,0,-1):
        A[i] = A[i - 1]
    A[0] = tmp
    return A
data = []
for _ in range(4):
    data.append(list(map(int,list(sys.stdin.readline().rstrip()))))
K = int(sys.stdin.readline())
for _ in range(K):
    spin_list = [0, 0, 0, 0]
    spin = (list(map(int,sys.stdin.readline().split())))
    spin_list[spin[0]-1] = spin[1]
    if spin[0]-1 == 0:
        for i in range(0,3):
            if data[i][2] != data[i+1][-2]:
                spin_list[i+1] = spin_list[i] * -1
            else:
                break
    elif spin[0]-1 == 0:
        for i in range(4,0,-1):
            if data[i][-2] != data[i-1][2]:
                spin_list[i-1] = spin_list[i] * -1
            else:
                break
    else:
        for i in range(spin[0]-1,3):
            if data[i][2] != data[i+1][-2]:
                spin_list[i+1] = spin_list[i] * -1
            else:
                break
        for i in range(spin[0]-1,0,-1):
            if data[i][-2] != data[i-1][2]:
                spin_list[i-1] = spin_list[i] * -1
            else:
                break
    for z in range(len(spin_list)):
        if spin_list[z] == 1:
            data[z] = spin_right(data[z])
        elif spin_list[z] == -1:
            data[z] = spin_left(data[z])
score = 0
for i in range(len(data)):
    if data[i][0] == 1:
        score += pow(2,i)
print(score)