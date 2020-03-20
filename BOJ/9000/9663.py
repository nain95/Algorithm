import sys
N = int(sys.stdin.readline().rstrip())
check1 = [0 for _ in range(N)]
check2 = [0 for _ in range(N*2)]
check3 = [0 for _ in range(N*2)]
result = 0
def solution(cur):
    if cur == N:
        global result
        result += 1
        return
    for i in range(N):
        if(check1[i] or check2[i+cur] or check3[cur-i+N]):
            continue
        check1[i] = 1
        check2[cur+i] = 1
        check3[cur-i+N] =1
        solution(cur+1)
        check1[i] = 0
        check2[cur + i] = 0
        check3[cur - i + N] = 0

    return result
print(solution(0))