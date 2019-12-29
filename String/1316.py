import sys
num = int(sys.stdin.readline().rstrip())
result = 0
for i in range(num):
    input_string = sys.stdin.readline().rstrip()
    temp = []
    for j in range(len(input_string)):
        if input_string[j] not in temp:
            temp.append(input_string[j])
        elif temp[-1] == input_string[j] and j == len(input_string)-1:
            result+=1
            break
        elif temp[-1] == input_string[j]:
            continue
        else:
            break
        if j == len(input_string)-1:
            result+=1
print(result)