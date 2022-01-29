import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
lines = [list(map(int, input().split())) for _ in range(n)]
lines.sort()
answer = []
cur_start, cur_end, cur_cost = lines[0]
for line in lines[1:]:
    start, end, cost = line
    if cur_end < start:
        answer.append([cur_start, cur_end, cur_cost])
        cur_start, cur_end, cur_cost = start, end, cost
        continue
    cur_end = max(end, cur_end)
    cur_cost = min(cost, cur_cost)
else:
    answer.append([cur_start, cur_end, cur_cost])
print(len(answer))
for i in answer:
    print(*i)