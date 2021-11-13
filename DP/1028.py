import sys, copy
sys.stdin = open('input.txt')
input = sys.stdin.readline

r, c = map(int, input().split())
# 메모리 초과 코드
# dp_down = [[] for _ in range(min(r, c)//2 + 1)]
# dp_up = [[] for _ in range(min(r, c)//2 + 1)]
# mine_map = []
#
# for _ in range(r):
#     mine_map.append(list(str(input())))
#
# for k in range(min(r, c)//2 + 1):
#     if k == 0:
#         for i in range(r):
#             for j in range(c):
#                 if mine_map[i][j] == '1':
#                     dp_up[k].append((i, j))
#                     dp_down[k].append((i, j))
#     else:
#         for row, col in dp_up[k-1]:
#             if row < r-k and k-1 < col < c-k:
#                 if mine_map[row+k][col-k] == '1' and mine_map[row+k][col+k] == '1':
#                     dp_up[k].append((row, col))
#         for row, col in dp_down[k-1]:
#             if k < row and k-1 < col < c-k:
#                 if mine_map[row-k][col-k] == '1' and mine_map[row-k][col+k] == '1':
#                     dp_down[k].append((row, col))
#
# answer = 0
# for k in range(min(r, c)//2, 0, -1):
#     if answer > k:
#         print(answer)
#         break
#     if len(dp_up[k]) == 0 or len(dp_down[k]) == 0:
#         continue
#     else:
#         for row, col in dp_up[k]:
#             if (row + 2*k, col) in dp_down[k]:
#                 answer = k+1
# else:
#     print(answer)

mine_map = []
dp = [[[0, 0]] * c for _ in range(r)]

for _ in range(r):
    mine_map.append(list(str(input())))

for k in range(min(r, c)//2 + 1):
    if k == 0:
        for i in range(r):
            for j in range(c):
                if mine_map[i][j] == '1':
                    dp[i][j] = [1, 1]
    else:
        for i in range(r):
            for j in range(c):
                up, down = dp[i][j]
                if up == k and i < r-k and k-1 < j < c-k:
                    if mine_map[i+k][j-k] == '1' and mine_map[i+k][j+k] == '1':
                        up += 1
                if down == k and 2*k-1 < i and k-1 < j < c-k:
                    if mine_map[i-k][j - k] == '1' and mine_map[i-k][j + k] == '1':
                        down += 1
                dp[i][j] = [up, down]

MAX = 0
for i in range(r):
    for j in range(c):
        up, _ = dp[i][j]
        if up > MAX:
            for k in range(up-1, -1, -1):
                if i+k*2 < r:
                    _, down = dp[i+k*2][j]
                    if down >= k:
                        MAX = max(MAX, k+1)
print(MAX)
