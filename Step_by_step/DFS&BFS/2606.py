import sys
computer_num = int(sys.stdin.readline().rstrip())
linked = int(sys.stdin.readline().rstrip())
matrix = [[0]*(computer_num+1) for _ in range(computer_num+1)]
for _ in range(linked):
    temp = list(map(int,sys.stdin.readline().rstrip().split()))
    matrix[temp[0]][temp[1]] = 1
    matrix[temp[1]][temp[0]] = 1

def dfs(cur,foot):
    foot+=[cur]
    for link in range(len(matrix[cur])):
        if matrix[link][cur] and link not in foot:
            foot = dfs(link,foot)
    return foot

print(len(dfs(1,[]))-1)
