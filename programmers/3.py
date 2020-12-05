def solution(total_sp, skills):
    data = [[] for _ in range(len(skills)+2)]
    bottom_num = [0]*(len(skills)+2)    #최하위 스킬을 구하기 위한 배열
    top_num = [0]*(len(skills)+2)       #최상위 스킬을 구하기 위한 배열
    sum_data = [0]*(len(skills)+2)
    for skill in skills:
        data[skill[1]].append(skill[0])
        bottom_num[skill[0]] += 1
        top_num[skill[1]] += 1
    bottom = []                        #최하위 스킬
    top = 0                            #최상위 스킬
    for idx in range(1,len(bottom_num)):
        if bottom_num[idx] == 0:       #연결된 하위 스킬이 없는 경우
            bottom.append(idx)
        if top == 0 and top_num[idx] == 0: #연결된 상위 스킬이 없는 경우
            top = idx
    while sum(sum_data) != total_sp:
        for bn in bottom:
            sum_data[bn] += 1
            up = data[bn][0]
            while up != top:
                sum_data[up] += 1
                up = data[up][0]
            sum_data[up] += 1
    answer = sum_data[1:]
    return answer


print(solution(121,[[1, 2], [1, 3], [3, 6], [3, 4], [3, 5]]))