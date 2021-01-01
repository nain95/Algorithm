import sys

def dfs(c, cur, cnt):
    global answer
    if cur == n-1:
        if c == 67108863:
            answer += 1
        return
    elif cur < n:
        dfs(c | check[cur + 1], cur + 1, cnt)
        dfs(c, cur + 1, cnt)


n = int(sys.stdin.readline())
word = [sys.stdin.readline().rstrip() for _ in range(n)]
check = [0]*100
for i in range(n):
    for j in range(len(word[i])):
        check[i] |= (1 << (ord(word[i][j]) - 97))
answer = 0
dfs(0, -1, 0)
print(answer)
