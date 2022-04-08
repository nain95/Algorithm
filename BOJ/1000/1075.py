a = int(input())
b = int(input())
tmp = a//b
answer = 0
if tmp * b // 100 == a // 100:
    while tmp * b // 100 == a // 100:
        tmp -= 1
    tmp += 1
else:
    while tmp * b // 100 != a // 100:
        tmp += 1
print("{0:02d}".format((tmp) * b % 100))