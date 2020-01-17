N = int(input())
result_list = [1,1]+[-1]*(N-1)
def solve(n):
    if n >= 2:
        for i in range(2,n+1):
            result_list[i] = (result_list[i-1] + result_list[i-2])%15746
    return result_list[n]
print(solve(N))