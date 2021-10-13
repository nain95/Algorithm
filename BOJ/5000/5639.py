import sys
sys.setrecursionlimit(10**6)

def find(data):
    if not data:
        return
    if len(data) == 1:
        print(data[0])
        return
    root = 0
    left = 1
    right = len(data)
    for i in range(left, len(data)):
        if data[root] < data[i]:
            right = i
            break
    find(data[left:right])
    find(data[right:])
    find([data[root]])

num = []
while(True):
    try:
        num.append(int(sys.stdin.readline()))
    except:
        break
find(num)