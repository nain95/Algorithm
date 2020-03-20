import sys
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]
N,M,K = map(int,sys.stdin.readline().split())
A = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
tree = []
for i in range(N):
    tmp = []
    for j in range(N):
        tmp.append([5])
    tree.append(tmp)

for i in range(M):
    tmp = list(map(int,sys.stdin.readline().split()))
    tree[tmp[0]-1][tmp[1]-1].append(tmp[2])
for z in range(K):
    for i in range(N):
        for j in range(N):
            energy = 0
            if len(tree[i][j]) > 1:
                for t in range(len(tree[i][j]) - 1, 0, -1):
                    if tree[i][j][t] <= tree[i][j][0]:
                        tree[i][j][0] -= tree[i][j][t]
                        tree[i][j][t] += 1
                    else:
                        energy += tree[i][j].pop(t) // 2
            tree[i][j][0] += energy
    for i in range(N):
        for j in range(N):
            for t in range(len(tree[i][j]) - 1, 0, -1):
                if tree[i][j][t] % 5 == 0:
                    for d in range(8):
                        x, y = i + dx[d], j + dy[d]
                        if x >= 0 and y >= 0 and x < N and y < N:
                            tree[x][y].append(1)
    for i in range(N):
        for j in range(N): tree[i][j][0] += A[i][j]

cnt = 0
for i in range(N):
    for j in range(N):
        if len(tree[i][j])>1:
            cnt += len(tree[i][j])-1
print(cnt)
