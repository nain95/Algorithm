import sys
def solution(A):
    global max_data
    stack = [0]
    if A == []:
        return max(max_data,0)
    for i in range(1,len(A)):
        if stack == []:
            stack.append(i)
        elif A[stack[-1]] > A[i]:
            while A[stack[-1]] > A[i]:
                pop_data = stack.pop()
                right = i-1
                if stack == []:
                    left = 0
                else:
                    left = stack[-1] +1
                length = right - left +1
                height = A[pop_data]
                max_data = max(max_data,length*height)
                if stack == []:
                    break
            stack.append(i)
        else:
            stack.append(i)
    while stack != []:
        right = len(A)-1
        pop_data = stack.pop()
        if stack == []:
            left = 0
        else:
            left = stack[-1] + 1
        length = right - left +1
        height = A[pop_data]
        max_data = max(max_data, length * height)
        if stack == []:
            break
    return max_data

N = int(sys.stdin.readline())
data = []
for _ in range(N):
    data.append(int(sys.stdin.readline()))
min_data = min(data)
max_data = min_data * N
min_index = data.index(min_data)
if min_index ==0:
    result = solution(data[min_index+1:])
elif min_data == N-1:
    result = solution(data[:min_index])
else:
    result = max(solution(data[:min_index]),solution(data[min_index+1:]))
print(result)