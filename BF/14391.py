import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n, m = map(int, input().split())
paper = []
for _ in range(n):
    line = list(map(int, list(str(input().strip()))))
    paper.append(line)

answer = 0
for i in range(1 << n*m):
    total = 0
    bi_i = bin(i)[2:].zfill(n*m)
    for row in range(n):
        row_sum = 0
        for col in range(m):
            idx = row*m + col
            if bi_i[idx] == '0':
                row_sum = row_sum*10 + paper[row][col]
            else:
                total += row_sum
                row_sum = 0
        total += row_sum
    for col in range(m):
        col_sum = 0
        for row in range(n):
            idx = row*m + col
            if bi_i[idx] != '0':
                col_sum = col_sum*10 + paper[row][col]
            else:
                total += col_sum
                col_sum = 0
        total += col_sum
    answer = max(answer, total)

print(answer)