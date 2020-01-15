import sys

def count(n):
    countlist = [0, 0, 1, 1]
    if 1<=n and n<=3:
        return countlist[n]
    else:
        for i in range(4,n+1):
            min_num = countlist[i-1]+1
            if i%3 ==0:
                tmp = countlist[int(i/3)]+1
                min_num = min(min_num,tmp)
            elif i%2 ==0:
                tmp = countlist[int(i/2)] + 1
                min_num = min(min_num, tmp)
            countlist.append(min_num)
        return countlist[i]

a=int(sys.stdin.readline())
print(count(a))