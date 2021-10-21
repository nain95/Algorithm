import sys, copy
from collections import defaultdict, deque

n = 4
max_ans = 0

def fish_check(matrix: dict, x : int, y : int) -> bool:
    if x < 0 or y < 0 or x >= n or y >= n:
        return False
    elif matrix[x][y] == 0:
        return False
    return True

def shark_check(matrix: dict, x : int, y : int) -> bool:
    if x < 0 or y < 0 or x >= n or y >= n:
        return False
    elif matrix[x][y] == -1:
        return False
    return True

def fish_move(matrix : dict, location : dict) -> None:
    direction = {1 : [-1,0], 2:[-1,-1], 3:[0,-1], 4:[1,-1], 5:[1,0], 6:[1,1], 7:[0,1], 8:[-1,1]}
    for fish in sorted(location.keys()):
        if fish == 0:
            continue
        x, y, d = location[fish]
        nx, ny = x + direction[d][0], y + direction[d][1]
        for _ in range(8):
            if fish_check(matrix, nx, ny):
                break
            else:
                d += 1
                if d == 9:
                    d = 1
                nx, ny = x + direction[d][0], y + direction[d][1]
        location[fish][2] = d
        matrix[x][y] = matrix[nx][ny]
        matrix[nx][ny] = fish
        tmp = location[fish]
        location[fish] = [nx, ny, d]
        if matrix[x][y] != -1:
            location[matrix[x][y]][0] = x
            location[matrix[x][y]][1] = y

def shark_init(matrix : dict, location : dict) -> int:
    res = matrix[0][0]
    location[0] = [0, 0, -1]
    fish = matrix[0][0]
    location[0][2] = location[fish][2]
    del(location[fish])
    matrix[0][0] = 0
    return res

def shark_movable(matrix : dict, location : dict) -> list:
    direction = {1 : [-1,0], 2:[-1,-1], 3:[0,-1], 4:[1,-1], 5:[1,0], 6:[1,1], 7:[0,1], 8:[-1,1]}
    x, y, d = location[0]
    movable = []
    nx, ny = x + direction[d][0], y + direction[d][1]
    while nx >= 0 and ny >= 0 and nx < n and ny < n:
        if not shark_check(matrix, nx, ny):
            nx, ny = nx + direction[d][0], ny + direction[d][1]
            continue
        movable.append([nx,ny])
        nx, ny = nx + direction[d][0], ny + direction[d][1]
    return movable

def solve(matrix : dict, location : dict, ans : int) -> None:
    fish_move(matrix, location)
    movable = deque(shark_movable(matrix,location))
    if not movable:
        global max_ans
        max_ans = max(max_ans, ans)
        return 

    while movable:
        x, y = movable.popleft()
        shark_x, shark_y, _ = location[0]
        copy_matrix = copy.deepcopy(matrix)
        copy_location = copy.deepcopy(location)
        copy_matrix[shark_x][shark_y] = -1
        copy_location[0] = [x, y, location[matrix[x][y]][2]]     #[x좌표, y좌표, 그자리에 있던 물고기의 방향]
        del(copy_location[matrix[x][y]])
        copy_matrix[x][y] = 0
        solve(copy_matrix, copy_location, ans + matrix[x][y])


if __name__ == '__main__':
    matrix = defaultdict(dict)
    location = {}
    for x in range(n):
        tmp = list(map(int, sys.stdin.readline().split()))
        for y in range(0, len(tmp), 2):
            location[tmp[y]] = [x, y//2, tmp[y+1]] # {물고기번호 : [x좌표, y좌표, 방향]}
            matrix[x][y // 2] = tmp[y]              # {x좌표 : {y좌표 : 물고기 번호}}
    ans = shark_init(matrix, location)
    solve(copy.deepcopy(matrix), copy.deepcopy(location), ans)
    print(max_ans)