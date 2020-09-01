A = input()
B = input()
length = 100000
for i in range(length):
    if A[i] == B[i] == '1':
        print(1,end='')
    else:
        print(0,end='')
print()
for i in range(length):
    if A[i] == '1' or B[i] == '1':
        print(1,end='')
    else:
        print(0,end='')
print()
for i in range(length):
    if A[i] != B[i]:
        print(1,end='')
    else:
        print(0,end='')
print()
for i in range(length):
    if A[i]=='0':
        print(1,end='')
    else:
        print(0,end='')
print()
for i in range(length):
    if B[i]=='0':
        print(1,end='')
    else:
        print(0,end='')