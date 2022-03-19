import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
MAX = 30 + 2

paper = [[0] * MAX for _ in range(MAX)]

# 누적합
for _ in range(n):
    x, y = map(int, input().split())
    paper[y][x] += 1
    paper[y][x+10] += -1
    paper[y+10][x] += -1
    paper[y+10][x+10] += 1

for i in range(1, MAX):
    for j in range(1, MAX):
        paper[i][j] += paper[i][j-1]

for i in range(1, MAX):
    for j in range(1, MAX):
        paper[j][i] += paper[j-1][i]

for i in range(MAX):
    for j in range(MAX):
        paper[i][j] = 1 if paper[i][j] > 0 else 0

for i in range(1, MAX):
    for j in range(MAX):
        if paper[i][j]:
            paper[i][j]=paper[i-1][j]+1

max_size = 0

for r in range(MAX):
    row = paper[r]
    pre_idx_stack = [0]
    for c in range(1, MAX):
        while pre_idx_stack and row[pre_idx_stack[-1]] > row[c]:
            h = row[pre_idx_stack[-1]]
            pre_idx_stack.pop()
            max_size = max(max_size, (c - pre_idx_stack[-1] - 1) * h)
        pre_idx_stack.append(c)
    max_size = max(max_size, (MAX - 1 - pre_idx_stack[-1] - 1) * row[pre_idx_stack[-1]])

print(max_size)


