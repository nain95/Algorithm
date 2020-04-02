import sys
T = sys.stdin.readline().rstrip()
B = sys.stdin.readline().rstrip()
T_len = len(T)
B_len = len(B)

check = []
check_len = 0
i = 0

while i < T_len:
    check.append(T[i])
    check_len += 1
    i += 1
    if check_len >= B_len:
        for j in range(-1,-B_len-1,-1):
            if check[j] != B[j]:
                break
        else:
            a = 0
            while a < B_len:
                check.pop()
                check_len -= 1
                a += 1
if check:
    print(''.join(check))
else:
    print("FRULA")