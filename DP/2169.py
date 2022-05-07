import sys
from collections import deque

sys.stdin = open('../input.txt')
input = sys.stdin.readline

n, m = map(int, input().split())
ground = [list(map(int, input().split())) for _ in range(n)]

dp = [[-999999] * m for _ in range(n)]

# init dp
a = 0
for i, c in enumerate(ground[0]):
    a += c
    dp[0][i] = a

for index, line in enumerate(dp[:-1]):
    ground_line = ground[index + 1]
    next_line = list(map(sum, zip(line, ground_line)))
    right, left = [-999999] * m, [-999999] * m
    # right
    for i in range(m):
        if i == 0:
            right[i] = next_line[i]
        else:
            right[i] = max(next_line[i], right[i-1] + ground_line[i])
    # left
    if index == n-1:
        continue
    for i in range(m-1, -1, -1):
        if i == m-1:
            left[i] = next_line[i]
        else:
            left[i] = max(next_line[i], left[i+1] + ground_line[i])
    for i, d in enumerate(map(max, zip(right, left))):
        dp[index+1][i] = d

print(dp[-1][-1])
