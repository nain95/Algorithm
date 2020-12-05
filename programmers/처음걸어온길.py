import sys
def solution(dirs):
    answer = 0
    min_value = 0
    max_value = 10
    visited = [[[[0]*11 for _ in range(11)] for _ in range(11)] for _ in range(11)]
    cur = [5,5]
    for dir in dirs:
        x, y = cur[0], cur[1]
        chk = False
        if dir == 'U':
            if cur[1] + 1 <= max_value:
                cur[1] += 1
                chk = True
        elif dir == 'D':
            if cur[1] - 1 >= min_value:
                cur[1] -= 1
                chk = True
        elif dir == 'L':
            if cur[0] - 1 >= min_value:
                cur[0] -= 1
                chk = True
        else:
            if cur[0] + 1 <= max_value:
                cur[0] += 1
                chk = True
        if chk:
            if not visited[x][y][cur[0]][cur[1]]:
                visited[x][y][cur[0]][cur[1]] = 1
                visited[cur[0]][cur[1]][x][y] = 1
                answer+=1
    return answer

print(solution("LLLLLLLLLRRRRRR"))