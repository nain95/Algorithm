import sys
N = int(sys.stdin.readline())
cnt = 0
range = 1
tmp = 1
if N == 1:
    print(1)
    sys.exit()
while 1:
    if range >= N:
        break
    tmp = 6*cnt
    cnt += 1
    range+= tmp
print(cnt)