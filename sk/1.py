def computeLPS(pat, lps):
    leng = 0
    i = 1
    while i < len(pat):
        if pat[i] == pat[leng]:
            leng += 1
            lps[i] = leng
            i += 1
        else:
            if leng != 0:
                leng = lps[leng-1]
            else:
                lps[i] = 0
                i += 1
    return lps

def KMPSearch(pat, txt):
    lps = computeLPS(pat, [0 for _ in range(len(pat))])
    i = 0
    j = 0
    while i < len(txt):
        if pat[j] == txt[i]:
            i += 1
            j += 1
        elif pat[j] != txt[i]:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1
        if j == len(pat):
            return True
    return False

def solution(goods):
    answer = []
    for idx, good in enumerate(goods):
        answer.append([])
        for length in range(1, len(good) + 1):
            for i in range(len(good) - length + 1):
                pattern = good[i : i + length]
                if pattern in answer[idx]:
                    continue
                for idx_2, good_2 in enumerate(goods):
                    if idx == idx_2:
                        continue
                    if KMPSearch(pattern, good_2):
                        break
                else:
                    answer[idx].append(pattern)
            if answer[idx]:
                answer[idx] = " ".join(sorted(answer[idx]))
                break
        else:
            answer[idx] = "None"
    return answer

print(solution(["a","b","c","d"]))