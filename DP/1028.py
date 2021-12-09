import sys, copy
sys.stdin = open('input.txt')
input = sys.stdin.readline

r, c = map(int, input().split())
dp_right_down = [[0] * c for _ in range(r)]
dp_left_down = [[0] * c for _ in range(r)]
mine_map = []
for _ in range(r):
    mine_map.append(list(str(input().strip())))

for i in range(c):
    dp_right_down[0][i] = int(mine_map[0][i])
    dp_left_down[0][i] = int(mine_map[0][i])

for row in range(1, r):
    for col in range(c):
        if mine_map[row][col] == '1':
            dp_right_down[row][col] = dp_right_down[row-1][col-1] + 1 if col > 0 else 1
            dp_left_down[row][col] = dp_left_down[row-1][col+1] + 1 if col < c-1 else 1

answer = 0
for row in range(r):
    for col in range(c):
        if dp_left_down[row][col] <= answer:
            continue
        else:
            for i in range(dp_left_down[row][col], answer, -1):
                try:
                    if dp_right_down[row][col+(i-1)*2] >= i and dp_left_down[row+i-1][col+i-1] >= i and dp_right_down[row+i-1][col+i-1] >= i:
                        answer = i
                        break
                except:
                    continue

print(answer)