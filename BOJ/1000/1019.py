import sys

def calc(n):
    while n > 0 :
        ans[n%10] += 1*pow(10,chk)
        n = n // 10


ans = [0]*10
start = 1
end = int(sys.stdin.readline())
data = [0]*10
chk = 0
sum = 0
while 1:
    while start % 10 != 0 or end % 10 != 9:
        if start == end:
            calc(start)
            for i in ans:
                print(i+sum,end= ' ')
            sys.exit()
        if start %10 != 0:
            calc(start)
            start += 1
        if start == end:
            calc(start)
            for i in ans:
                print(i+sum,end= ' ')
            sys.exit()
        if end % 10 != 9:
            calc(end)
            end-=1
        if start == end:
            calc(start)
            for i in ans:
                print(i+sum,end= ' ')
            sys.exit()
    chk += 1
    end //= 10
    start //= 10
    sum += (end-start+1)*pow(10,chk-1)


