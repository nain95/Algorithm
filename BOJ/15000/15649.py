import sys
N,M = map(int,(sys.stdin.readline().rstrip().split()))
check = [False for _ in range(N + 1)]
arr = [0 for _ in range(M)]

def solution(idx, N, M):
    if idx == M:
        for i in range(M):
            print(arr[i], end=" ")
        print()

        return

    for i in range(1, N + 1):
        if check[i]:
            continue

        check[i], arr[idx] = True, i
        solution(idx + 1, N, M)
        check[i] = False

solution(0, N, M)