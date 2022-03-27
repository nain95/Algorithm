import sys

first = sys.stdin.readline().rstrip()
second = sys.stdin.readline().rstrip()
answer = 0
dp = [[0 for _ in range(len(second))] for _ in range(len(first))]

for i in range(len(first)):
    for j in range(len(second)):
        if first[i] == second[j]:
            if i == 0:
                dp[0][j] = 1
                if dp[i][0] > answer:
                    answer = 1
            elif j == 0:
                dp[i][0] = 1
                if dp[0][j] > answer:
                    answer = 1
            else:
                dp[i][j] = dp[i-1][j-1] + 1
                if dp[i][j] > answer: 
                    answer = dp[i][j]
print(answer)
