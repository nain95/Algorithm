import sys
import bisect
from _collections import defaultdict
sys.setrecursionlimit(10000)

def solve(i, j):
    if i > j:
        return 0
    elif i == j:
        return 1
    if dp[i][j] != -1:
        return dp[i][j]
    dp[i][j] = 2
    d = number[j] - number[i]
    nxt = number[j] + d
    idx = bisect.bisect_left(number, nxt)
    if idx < len(number) and number[idx] == nxt:
        dp[i][j] = solve(j, idx) + 1
        return dp[i][j]
    return dp[i][j]


dp = [[-1]*2001 for _ in range(2001)]
num = int(sys.stdin.readline())
number = list(int(sys.stdin.readline()) for _ in range(num))
dic = defaultdict(int)
for i in number:
    dic[i] += 1
answer = max(dic.values())
number = sorted(list(set(number)))
for i in range(len(number)-1):
    for j in range(i+1,len(number)):
        answer = max(answer, solve(i,j))
print(answer)