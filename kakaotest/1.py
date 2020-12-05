from _collections import deque

def bfs(cur, des):
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    check = [[0]*3 for _ in range(4)]
    cur -= 1
    des -= 1
    cur_row = cur//3
    des_row = des//3
    if cur_row == 0:
        cur_col = cur
    else:
        cur_col = cur % (cur_row*3)
    if des_row == 0:
        des_col = des
    else:
        des_col = des % (des_row*3)
    queue = deque([[cur_row,cur_col]])
    cnt = 0
    while queue:
        size = len(queue)
        for _ in range(size):
            curxy = queue.popleft()
            curx = curxy[0]
            cury = curxy[1]
            check[curx][cury] = 1
            if curx == des_row and cury ==des_col:
                return cnt
            else:
                for i in range(4):
                    nx,ny = curx + dx[i] , cury + dy[i]
                    if 0 <= nx < 4 and 0 <= ny < 3 and check[nx][ny] != 1:
                        queue.append([nx,ny])
        cnt+=1


def solution(numbers, hand):
    answer = ''
    left = 10
    right = 12
    for i in numbers:
        if i == 0:
            i = 11
        if i == 1 or i == 4 or i == 7:
            answer += 'L'
            left = i
        elif i == 3 or i == 6 or i == 9:
            answer += 'R'
            right = i
        else:
            left_dis = bfs(left,i)
            right_dis = bfs(right,i)
            if left_dis < right_dis:
                answer += 'L'
                left = i
            elif left_dis > right_dis:
                answer += 'R'
                right = i
            else:
                if hand == 'left':
                    answer += 'L'
                    left = i
                else:
                    answer += 'R'
                    right = i
    return answer

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5],"right"))
