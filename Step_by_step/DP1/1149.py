import sys

def RGB(n,cost):
    min_cost = [[] for i in range(n)]
    for i in range(n):
        if i == 0:
            min_cost[0].append(cost[0][0])
            min_cost[0].append(cost[0][1])
            min_cost[0].append(cost[0][2])
        else:
            for j in range(3):
                if j == 0:
                    min_cost[i].append(cost[i][j]+min(min_cost[i-1][1],min_cost[i-1][2]))
                elif j == 1:
                    min_cost[i].append(cost[i][j]+min(min_cost[i-1][0],min_cost[i-1][2]))
                elif j == 2:
                    min_cost[i].append(cost[i][j]+min(min_cost[i-1][0],min_cost[i-1][1]))
    return (min(min_cost[n-1]))

b=[]
a=int(sys.stdin.readline())
for i in range(a):
    b.append(list(map(int,sys.stdin.readline().split())))
print(RGB(a,b))