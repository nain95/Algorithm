def solution(self, numbers):
    if len(numbers) == 1:
        return numbers[0]
    elif len(numbers) == 2:
        return max(numbers) - min(numbers)
    s = 0
    e = -1
    a = numbers[s] + len(numbers[s+1:])//2
    return

print(solution(1,[3,1,1,9,4]))
