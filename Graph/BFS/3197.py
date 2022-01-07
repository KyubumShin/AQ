import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline

r, c = map(int, input().split())
obj = {'.': 1, 'L': 2, 'X': 0}
table = []
swan = []
ice = []
for i in range(r):
    lst = list(map(lambda x: obj[x], list(input().strip())))
    for j in lst:
        if i == 0:
            ice.append([j, i])
        elif i == 2:
            swan.append([j, i])
    table.append(lst)
print(table)
print(swan)
print(ice)

def bfs(queue):
    pass



