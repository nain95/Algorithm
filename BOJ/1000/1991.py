import sys
from collections import defaultdict, deque

class Node():
    def __init__(self, key, left, right):
        self.key = key
        self.left = left
        self.right = right

def preorder(start):
    print(start,end='')
    if tree[start].left != '.':
        preorder(tree[start].left)
    if tree[start].right != '.':
        preorder(tree[start].right)

def inorder(start):
    if tree[start].left != '.':
        inorder(tree[start].left)
    print(start,end='')
    if tree[start].right != '.':
        inorder(tree[start].right)

def postorder(start):
    if tree[start].left != '.':
        postorder(tree[start].left)
    if tree[start].right != '.':
        postorder(tree[start].right)
    print(start,end='')

n = int(sys.stdin.readline())
tree = {}
for _ in range(n):
    node, left, right = sys.stdin.readline().split()
    tree[node] = Node(node, left, right)
preorder('A')
print()
inorder('A')
print()
postorder('A')