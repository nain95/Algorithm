import sys
sys.setrecursionlimit(10000)
"""
[0,  0,  0,  0,  0,  0]
[0, 50, 45, 37, 32, 30]
[0, 35, 50, 40, 20, 25]
[0, 30, 30, 25, 17, 28]
[0, 27, 24, 22, 15, 10]

"""
dx = [1,-1,0,0]
dy = [0,0,1,-1]
M,N = map(int,sys.stdin.readline().split())
data = [[0]*(N+2)]
dp = [[-1]*(N+2) for _ in range(M+2)]
for _ in range(M):
    data.append([0]+list(map(int,sys.stdin.readline().split()))+[0])
data.append([0]*(N+2))
def search(x,y):
    if x == M and y == N:
        return 1
    if dp[x][y] == -1:
        dp[x][y] = 0
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if data[nx][ny] != -1:
                if data[nx][ny] < data[x][y] and nx >0 and nx <= M and ny >0 and ny <= N:
                    dp[x][y] += search(nx,ny)
    return dp[x][y]
search(1,1)
print(dp[1][1])