import sys
sys.setrecursionlimit(10**5)

def ccw(a, b, c):
    x1, y1, x2, y2, x3, y3 = a + b + c
    tmp = (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)
    if tmp > 0:
        return 1
    elif tmp < 0:
        return -1
    else:
        return 0

def line_cross_discrimination(a_line: tuple, b_line: tuple):
    a = a_line[:2]
    b = a_line[2:]
    c = b_line[:2]
    d = b_line[2:]
    ccw_mul_res1 = ccw(a, b, c) * ccw(a, b, d)
    ccw_mul_res2 = ccw(c, d, a) * ccw(c, d, b)
    if ccw_mul_res1 == 0 and ccw_mul_res2 == 0:
            if a <= d and b >= c:
                return 1
    elif ccw_mul_res1 <= 0 and ccw_mul_res2 <= 0:
        return 1
    return 0

def dfs(now):
    visited[now] = 1
    for i in range(len(holecanmouse[now])):
        tmp = holecanmouse[now][i]
        if work[tmp] == 0 or (visited[work[tmp]] == 0 and dfs(work[tmp])):
            work[tmp] = now
            return True
    return False

if __name__ == '__main__':
    n, k, h, m = map(int, sys.stdin.readline().split())
    pos_list = []
    line_list = []
    hole_pos = []
    holecanmouse = [[] for _ in range(h)]
    for _ in range(n):
        x, y = map(int, sys.stdin.readline().split())
        pos_list.append((x,y))
    for idx in range(n):
        pos_x1, pos_y1, pos_x2, pos_y2 = pos_list[idx] + pos_list[(idx + 1) % n]
        if (pos_x1, pos_y1) > (pos_x2, pos_y2):
            pos_x1, pos_x2 = pos_x2, pos_x1
            pos_y1, pos_y2 = pos_y2, pos_y1
        line_list.append((pos_x1, pos_y1, pos_x2, pos_y2))
    for _ in range(h):
        hole_pos.append(tuple(map(int, sys.stdin.readline().split())))
    for idx in range(m):
        original_pos_x, original_pos_y = map(int,sys.stdin.readline().split())
        for hole_idx, hole in enumerate(hole_pos):
            pos_x, pos_y = original_pos_x, original_pos_y
            hole_x, hole_y = hole
            chk = 1
            if hole in pos_list:
                chk = 2
            if (pos_x, pos_y) > (hole_x, hole_y):
                pos_x, hole_x = hole_x, pos_x
                pos_y, hole_y = hole_y, pos_y
            cnt = 0
            for line in line_list:
                if line_cross_discrimination((pos_x, pos_y, hole_x, hole_y), line):
                    cnt += 1
            if cnt == chk:
                holecanmouse[hole_idx].append(idx)
    work = [0] * m
    visited = [0] * h
    count = 0
    for i in range(h):
        for _ in range(k):
            for j in range(h):
                visited[j] = 0
            if (dfs(i)):
                count+=1
    # print(count)
    if count >= m:
        print("Possible")
    else:
        print("Impossible")
