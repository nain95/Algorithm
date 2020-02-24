import sys,itertools,copy
def chicken_length(check):
    result = 0
    for i in home:
        min_length = sys.maxsize
        for j in chicken:
            if j in check:
                continue
            min_length = min(min_length,abs(i[0]-j[0])+abs(i[1]-j[1]))
        result += min_length
    return result

def solve(cur):
    global result_length
    chicken_com = list(itertools.combinations(chicken, len(chicken)-M))
    while chicken_com:
        check = chicken_com.pop()
        result_length = min(result_length,chicken_length(check))



N,M = map(int,sys.stdin.readline().split())
map_data = []
home = []
chicken = []
result_length = sys.maxsize
for i in range(N):
    temp = list(map(int,sys.stdin.readline().split()))
    map_data.append(temp)
    for j in range(N):
        if map_data[i][j] == 1:
            home.append([i,j])
        elif map_data[i][j] == 2:
            chicken.append([i,j])
solve(0)
print(result_length)