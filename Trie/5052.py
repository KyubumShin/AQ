import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}


class Trie(object):
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        curr_node = self.head
        for char in string:
            if char not in curr_node.children:
                curr_node.children[char] = Node(char)
            curr_node = curr_node.children[char]
            if curr_node.data is not None:
                return False
        curr_node.data = string
        return True


t = int(input())

for _ in range(t):
    trie = Trie()
    n = int(input())
    num_list = []
    for _ in range(n):
        number = input().strip()
        num_list.append(number)
    num_list.sort(key=lambda x: len(x))
    for num in num_list:
        check = trie.insert(num)
        if not check:
            print('NO')
            break
    else:
        print('YES')
