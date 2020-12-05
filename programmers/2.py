def solution(n):
    answer_data = [1]
    num = 3
    while len(answer_data) <= n:
        answer_data.append(num)
        append_data = []
        for i in answer_data[:-1]:
            append_data.append(i+num)
        answer_data += append_data
        num *= 3
    answer = answer_data[n-1]
    return answer


print(solution(4))
print(solution(11))