import sys
input_string = sys.stdin.readline().rstrip()
Croatia = ["c=","c-","dz=","d-","lj","nj","s=","z="]
for i in Croatia:
    if i in input_string:
        input_string = input_string.replace(i,"a",input_string.count(i))
print(len(input_string))