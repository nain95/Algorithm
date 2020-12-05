import math

def solution(self, x, y1, y2):
    ans = 0
    for i in range(len(x)):
        ans += math.degrees(math.atan(y1[i]/x[i]) + math.atan(y2[i]/x[i]))/180
    return 1
print(solution(1,[1,2],[-1,-2],[1,2]))