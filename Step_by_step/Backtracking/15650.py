import sys
N,M = map(int,(sys.stdin.readline().rstrip().split()))
check = [False for _ in range(N + 1)]
arr = [0 for _ in range(M)]

def solution(cnt,cur):
    if cnt == M:
        for i in range(M):
            print(arr[i], end=" ")
        print()
        return

    for i in range(cur, N + 1):
        if check[i]:
            continue

        check[i], arr[cnt] = True, i
        solution(cnt + 1, i+1)
        check[i] = False

solution(0,1)
