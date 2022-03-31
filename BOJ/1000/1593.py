import sys

def solution(g,s,W,S):
    answer = 0
    list1 = [0] * 27
    list2 = [0] * 27
    list1_tmp = [0] * 27
    list2_tmp = [0] * 27

    for w in W:
        if 'a' <= w <= 'z':
            list1[ord(w) - 97] += 1
        else:
            list2[ord(w) - 65] += 1
    length = 0
    start = 0
    end = 0
    for i in range(s):
        if 'a' <= S[i] <= 'z':
            list1_tmp[ord(S[i]) - ord('a')] += 1
        else:
            list2_tmp[ord(S[i]) - ord('A')] += 1
        length += 1
        if length == g:
            if list1 == list1_tmp and list2 == list2_tmp:
                answer+=1
            if 'a' <= S[start] <= 'z':
                list1_tmp[ord(S[start]) - ord('a')] -= 1
            else:
                list2_tmp[ord(S[start]) - ord('A')] -= 1
            start += 1
            length -= 1
    print(answer)
g, s = map(int,(sys.stdin.readline().split()))
W = sys.stdin.readline().rstrip()
S = sys.stdin.readline().rstrip()
solution(g,s,W,S)