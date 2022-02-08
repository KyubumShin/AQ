import sys, math
sys.stdin = open('./input.txt')
input = sys.stdin.readline

n = int(input())

for i in range(n):
    tree = input().strip()
    if '[' not in tree:
        print(1)
        continue
    max_level = 0
    cur_level = 0
    for s in tree:
        if s == '[':
            cur_level += 1
        else:
            cur_level -= 1
        max_level = max(max_level, cur_level)
    print(2 ** max_level)