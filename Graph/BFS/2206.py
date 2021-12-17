import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
n, m = map(int, input().split())
array = []
visit = [[[0, 0] for _ in range(m)]for _ in range(n)]
for _ in range(n):
    line = list(input().strip())
    array.append(line)
queue = deque([[0, 0, True]])
visit[0][0][0] = 1
while queue:
    x, y, can_break = queue.popleft()
    if x == m-1 and y == n-1:
        print(visit[y][x][int(can_break)]+1)
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < m and 0 <= ny < n and visit[ny][nx][int(can_break)] == 0:
            if array[ny][nx] == '1' and can_break:
                queue.append([nx, ny, False])
                visit[ny][nx][0] = 1 + visit[y][x][int(can_break)]
            if array[ny][nx] == '0':
                queue.append([nx, ny, can_break])
                visit[ny][nx][int(can_break)] = 1 + visit[y][x][int(can_break)]
else:
    print(-1)