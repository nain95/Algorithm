def solution(n, money):
    money = sorted(money)
    dp = [0] * (n+1)
    for i in range(len(money)):
        for j in range(1,n+1):
            if money[i] == j or money[i] == 1:
                dp[j] += 1
            elif j >= money[i]:
                dp[j] = (dp[j] + dp[j-money[i]]) % 1000000007
    return dp[-1]
print(solution(4,[1,2]))