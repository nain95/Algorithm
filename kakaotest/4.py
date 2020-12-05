import sys,copy
def dfs(board,cur,des,stack,visit,board_x,board_y,matrix):
    global minleng,minstack
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    visit[cur[0]][cur[1]] = 1
    stack.append(cur)
    if cur == des:
        if len(stack) < minleng:
            minleng = len(stack)
            print(stack)
            minstack = []
            minstack = copy.deepcopy(stack)
        elif len(stack) == minleng:
            minstack.append(stack)
        stack.pop()

        return stack
    else:
        for i in range(4):
            nx,ny=cur[0]+dx[i],cur[1]+dy[i]
            if 0 <= nx <= board_x and 0 <= ny <= board_y and visit[nx][ny] == 0 and board[nx][ny] == 0:
                dfs(board,[nx,ny],des,stack,visit,board_x,board_y,matrix)
                visit[nx][ny] = 0
        stack.pop()

def solution(board):
    global minstack
    answer = 0
    matrix = [[0]*len(board[0]) for _ in range(len(board))]
    stack = []
    board_x,board_y = len(board)-1,len(board[0])-1
    visit = [[0]*len(board[0]) for _ in range(len(board))]
    print(dfs(board,[0,0],[board_x,board_y],stack,visit,board_x,board_y,matrix))
    print(minstack)
    return answer
minleng = sys.maxsize
minstack = []

solution([[0,0,0],[0,0,0],[0,0,0]])