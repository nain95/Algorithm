import sys
N,K = map(int,sys.stdin.readline().rstrip().split())
coin = []
for _ in range(N):
    coin.append(int(sys.stdin.readline().rstrip()))
coin_cnt = 0
while K!=0 or coin != []:
    if coin[-1] <= K:
        tmp = K//coin[-1]
        K-=coin[-1]*tmp
        coin_cnt+=tmp
        coin.pop()
    else:
        coin.pop()
print(coin_cnt)