class Node:
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}

class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        curr_node = self.head

        for char in string:
            if char not in curr_node.children:
                curr_node.children[char] = Node(char)

            if curr_node.data:
                return False
            curr_node = curr_node.children[char]
        curr_node.data = string
        return True

    # def search(self, string):
    #     curr_node = self.head

    #     for char in string:
    #         if char in curr_node.children:
    #             curr_node = curr_node.children[char]
    #         else:
    #             return False

    #     if curr_node.data is not None:
    #         return True
import sys

t = int(sys.stdin.readline())
for _ in range(t):
    tr = Trie()
    n = int(sys.stdin.readline())
    number_list = []
    for _ in range(n):
        number_list.append(sys.stdin.readline().rstrip())
    number_list = sorted(number_list, key=lambda x:len(x))
    for number in number_list:
        if not tr.insert(number):
            print('NO')
            break
    else:
        print('YES')
    

    
