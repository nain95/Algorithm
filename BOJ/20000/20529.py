import sys
from collections import defaultdict
from itertools import combinations


def counting(a, b, c):
    return len(set(list(a) + list(b))) + len(set(list(b) + list(c))) + len(set(list(c) + list(a))) - 12


t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    data = list(sys.stdin.readline().split())
    if n > 32:
        print(0)
    else:
        dic = defaultdict(int)
        for mbti in data:
            dic[mbti] += 1
            if dic[mbti] == 3:
                print(0)
                break
        else:
            tmp = sorted(dic.items(), key=lambda x: x[1], reverse=True)
            ans = 200
            if tmp[0][1] >= 3:
                ans = 0
            else:
                for a, b, c in combinations(data, 3):
                    ans = min(ans, counting(a, b, c))
            print(ans)
