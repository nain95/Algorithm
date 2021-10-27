import sys
sys.setrecursionlimit(10**5)

def find(in_x, in_y, pre_x, pre_y):
    if pre_x > pre_y :
        return
    root = order[1][pre_y]
    print(root, end = ' ')
    in_root = -1
    for i in range(in_x, in_y + 1):
        if order[0][i] == root:
            in_root = i
            break
    if in_root == in_y:
        find(in_x, in_root - 1, pre_x, pre_y - 1)
        return
    elif in_root == in_x:
        find(in_x + 1, in_y, pre_x, pre_y - 1)
        return
    pre_right = pre_x
    if in_root < n-1:
        for i in range(pre_x, pre_y):
            if order[1][i] == order[0][in_root + 1]:
                pre_right = i
                break
    find(in_x, in_root - 1, pre_x, pre_right - 1)
    find(in_root + 1, in_y, pre_right, pre_y - 1)


n = int(sys.stdin.readline())
order = []  # [0] : inorder , [1] : preorder
for _ in range(2):
    order.append(list(map(int, sys.stdin.readline().split())))
find(0, n-1, 0, n-1)
