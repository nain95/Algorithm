import sys


def makeTable(pattern):
    patternsize = len(pattern)
    table = [0] * patternsize
    j = 0
    for i in range(1,patternsize):
        while j > 0 and pattern[i] != pattern[j]:
            j = table[j-1]
        if pattern[i] == pattern[j]:
            j += 1
            table[i] = j
    return table


def kmp(parent, pattern):
    table = makeTable(pattern)
    parentsize = len(parent)
    patternsize = len(pattern)
    result = []
    j = 0
    for i in range(parentsize):
        while j > 0 and parent[i] != pattern[j]:
            j = table[j-1]
        if parent[i] == pattern[j]:
            if j == patternsize - 1:
                result.append(i - patternsize +2)
                j = table[j]
            else:
                j += 1
    return result
T = sys.stdin.readline().rstrip()
P = sys.stdin.readline().rstrip()
result = kmp(T,P)
print(len(result))
for i in result:
    print(i)