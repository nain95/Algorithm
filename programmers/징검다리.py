def solution(distance, rocks, n):
    rocks = sorted(rocks) + [distance]
    answer = 0
    left, right = 0, distance
    cur = 0
    while left <= right:
        mid = (left + right) // 2
        min_ans = float('inf')
        cnt = 0
        cur = 0
        for k in range(len(rocks)):
            if rocks[k] == cur:
                continue
            if rocks[k] - cur >= mid:
                min_ans = min(min_ans, rocks[k] - cur)
                cur = rocks[k]
            else:
                print(rocks[k])
                cnt += 1
        if cnt > n:
            right = mid - 1
        else:
            answer = min_ans
            left = mid + 1
    return answer
print(solution(25, [2, 14, 11, 21, 17], 2))