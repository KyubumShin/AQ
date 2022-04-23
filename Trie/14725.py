import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


class Node(object):
    def __init__(self, key, depth, data=None):
        self.key = key
        self.data = data
        self.depth = depth
        self.children = {}


class Trie(object):
    def __init__(self):
        self.head = Node(0, None)

    def insert(self, string):
        curr_node = self.head
        depth = 0
        for char in string:
            if char not in curr_node.children:
                curr_node.children[char] = Node(char, depth)
            curr_node = curr_node.children[char]
            if curr_node.data is not None:
                return False
            depth += 1
        curr_node.data = string
        return True

    def get(self):
        temp = []
        stack = [self.head]
        while stack:
            cur = stack.pop()
            temp.append([cur.depth, cur.key])
            for child in cur.children.values():
                stack.append(child)
        return temp


n = int(input())
ant = Trie()
lst = [list(input().split())[1:] for _ in range(n)]
for i in sorted(lst, reverse=True):
    ant.insert(i)

answer = ant.get()
for depth, key in answer[1:]:
    print('--'*depth + key)
