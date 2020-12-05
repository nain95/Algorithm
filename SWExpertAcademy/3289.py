import copy
from _collections import defaultdict

t = int(input())
for case in range(t):
    n, m = map(int,input().split())
    group = []
    visited = [0] * (n+1)
    dic = {}
    ans = ''
    for _ in range(m):
        input_data = list(map(int,input().split()))
        A, B = input_data[1],input_data[2]
        if input_data[0] == 0:
            if A == B:
                continue
            if visited[A] == 0 and visited[B] == 0:
                group.append([A,B])
                dic[A] = len(group)-1
                dic[B] = len(group)-1
            elif visited[A] == 1 and visited[B] == 0:
                group[dic[A]].append(B)
                dic[B] = copy.deepcopy(dic[A])
            elif visited[A] == 0 and visited[B] == 1:
                group[dic[B]].append(A)
                dic[A] = copy.deepcopy(dic[B])
            else:
                if dic[A] == dic[B]:
                    continue
                if len(group[dic[A]]) >= len(group[dic[B]]):
                    remove = dic[B]
                    for i in group[dic[B]]:
                        dic[i] = copy.deepcopy(dic[A])
                        group[dic[A]].append(i)
                    group[remove] = []
                else:
                    remove = dic[A]
                    for i in group[dic[A]]:
                        dic[i] = copy.deepcopy(dic[B])
                        group[dic[B]].append(i)
                    group[remove] = []
            visited[A] = 1
            visited[B] = 1
        else:
            if A == B:
                ans += '1'
            elif visited[A] == 0 or visited[B] == 0:
                ans += '0'
            elif dic[A] == dic[B]:
                ans += '1'
            else:
                ans += '0'
    print(f'#{case+1} {ans}')