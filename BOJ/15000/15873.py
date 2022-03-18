ans = 0
for i in list(map(int, list(input()))):
    if i == 0:
        ans += 9
    else:
        ans += i
print(ans)