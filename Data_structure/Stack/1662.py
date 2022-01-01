import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

s = input().strip()
stack = []
length = 0
temp = ''
for c in s:
    if c.isdigit():
        length += 1
        temp = c
    elif c == '(':
        stack.append((temp, length - 1))
        length = 0
    else:
        multi, prev_l = stack.pop()
        length = (int(multi) * length) + prev_l

print(length)