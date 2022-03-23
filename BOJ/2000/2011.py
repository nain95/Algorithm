n = input()
dp = [0, 1]
if n[0] == '0':
    print(0)
    exit()
for i in range(1, len(n)):
    if n[i] == '0' and (int(n[i-1]) != 1 and int(n[i-1]) != 2):
        print(0)
        exit()
    if int(n[i]) != 0 and int(n[i-1]) != 0 and int(n[i-1] + n[i]) <= 26 and ((i == len(n)-1) or (i < len(n)-1 and n[i+1] != '0')):
        if i == 1:
            dp.append((dp[-1] + 1) % 1000000)
        else: 
            dp.append((dp[-1] + dp[-2]) % 1000000)
    else:
        dp.append(dp[-1])
print(dp[-1])
