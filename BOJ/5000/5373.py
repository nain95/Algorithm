import sys


def left_spin(index):
    cube[index][0], cube[index][2], cube[index][6], cube[index][8] = cube[index][2], cube[index][8], cube[index][0], cube[index][6]
    cube[index][1], cube[index][3], cube[index][5], cube[index][7] = cube[index][5], cube[index][1], cube[index][7], cube[index][3]

def right_spin(index):
    cube[index][0], cube[index][2], cube[index][6], cube[index][8] = cube[index][6], cube[index][0], cube[index][8], cube[index][2]
    cube[index][1], cube[index][5], cube[index][7], cube[index][3] = cube[index][3], cube[index][1], cube[index][5], cube[index][7]


def left(spin):
    if spin == 0:
        right_spin(4)
        tmp = cube[3][0:7:3]
        for i in range(3, 0, -1):
            for j in range(3):
                cube[i][j * 3] = cube[i - 1][j * 3]
        for i in range(3):
            cube[0][i * 3] = tmp[i]
    else:
        left_spin(4)
        tmp = cube[0][0:7:3]
        for i in range(3):
            for j in range(3):
                cube[i][j*3] = cube[i+1][j*3]
        for i in range(3):
            cube[3][i*3] = tmp[i]


def right(spin):
    if spin == 0:
        right_spin(5)
        tmp = cube[0][2:9:3]
        for i in range(3):
            for j in range(3):
                cube[i][j*3+2] = cube[i+1][j*3+2]
        for i in range(3):
            cube[3][i*3+2] = tmp[i]
    else:
        left_spin(5)
        tmp = cube[3][2:9:3]
        for i in range(3, 0, -1):
            for j in range(3):
                cube[i][j*3+2] = cube[i - 1][j*3+2]
        for i in range(3):
            cube[0][i*3+2] = tmp[i]


def up(spin):
    if spin == 0:
        right_spin(0)
        tmp = cube[5][0:3]
        cube[5][0:3] = cube[3][8:5:-1]
        cube[3][6:9] = [cube[4][2]]+[cube[4][1]]+[cube[4][0]]
        cube[4][0:3] = cube[1][0:3]
        cube[1][0:3] = tmp
    else:
        left_spin(0)
        tmp = cube[5][2::-1]
        cube[5][0:3] = cube[1][0:3]
        cube[1][0:3] = cube[4][0:3]
        cube[4][0:3] = cube[3][8:5:-1]
        cube[3][6:9] = tmp


def down(spin):
    if spin == 0:
        right_spin(2)
        tmp = cube[5][8:5:-1]
        cube[5][6:9] = cube[1][6:9]
        cube[1][6:9] = cube[4][6:9]
        cube[4][6:9] = cube[3][2::-1]
        cube[3][:3] = tmp
    else:
        left_spin(2)
        tmp = cube[5][6:9]
        cube[5][6:9] = cube[3][2::-1]
        cube[3][0:3] = cube[4][8:5:-1]
        cube[4][6:9] = cube[1][6:9]
        cube[1][6:9] = tmp


def front(spin):
    if spin == 0:
        right_spin(1)
        tmp = cube[0][6:9]
        cube[0][6],cube[0][7],cube[0][8] = cube[4][8],cube[4][5],cube[4][2]
        cube[4][2],cube[4][5],cube[4][8] = cube[2][0],cube[2][1],cube[2][2]
        cube[2][:3] = cube[5][6::-3]
        cube[5][0],cube[5][3],cube[5][6] = tmp[0],tmp[1],tmp[2]
    else:
        left_spin(1)
        tmp = cube[0][6:9]
        cube[0][6:9] = cube[5][0:7:3]
        cube[5][0],cube[5][3],cube[5][6] = cube[2][2],cube[2][1],cube[2][0]
        cube[2][:3] = cube[4][2:9:3]
        cube[4][8],cube[4][5],cube[4][2] = tmp[0],tmp[1],tmp[2]


def back(spin):
    if spin == 0:
        right_spin(3)
        tmp = cube[0][:3]
        cube[0][:3] = cube[5][2:9:3]
        cube[5][8],cube[5][5],cube[5][2] = cube[2][6],cube[2][7],cube[2][8]
        cube[2][6:9] = cube[4][:7:3]
        cube[4][6],cube[4][3],cube[4][0] = tmp[0],tmp[1],tmp[2]
    else:
        left_spin(3)
        tmp = cube[0][:3]
        cube[0][:3] = cube[4][6::-3]
        cube[4][0],cube[4][3],cube[4][6] = cube[2][6],cube[2][7],cube[2][8]
        cube[2][6:] = cube[5][8]+cube[5][5]+cube[5][2]
        cube[5][2],cube[5][5],cube[5][8] = tmp[0],tmp[1],tmp[2]


t = int(sys.stdin.readline())
for _ in range(t):
    cube = [['w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w'], ['r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r'],
            ['y', 'y', 'y', 'y', 'y', 'y', 'y', 'y', 'y'], ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'],
            ['g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g'], ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']]

    n = int(sys.stdin.readline())
    spin_data = sys.stdin.readline().split()
    for i in spin_data:
        i = list(i)
        if i[1] == '-':
            i[1] = 1
        else:
            i[1] = 0
        if i[0] == 'L':
            left(i[1])
        elif i[0] == 'R':
            right(i[1])
        elif i[0] == 'U':
            up(i[1])
        elif i[0] == 'D':
            down(i[1])
        elif i[0] == 'F':
            front(i[1])
        else:
            back(i[1])
    for i in range(0,9,3):
        print(cube[0][i],end='')
        print(cube[0][i+1], end='')
        print(cube[0][i+2])
