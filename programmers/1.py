def solution(p):
    while 1:
        number = [0] * 10
        p+=1
        chk = True
        for i in str(p):
            int_i = int(i)
            if number[int_i] == 1:
                chk = False
                break
            else:
                number[int_i] = 1
        if chk:
            answer = p
            break
    return answer

print(solution(9900))