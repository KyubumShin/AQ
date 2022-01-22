import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

n, m, t = map(int, input().split())
route = [list(map(int, input().split())) for _ in range(n)]
print(route)
answer = float('inf')
queue = deque()
queue.append([0, 0, 0])


while queue:
    time, y, x = queue.popleft()
    if y == n-1 and x == m-1:
        answer = min(answer, time)
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < n and 0 <= nx < m:
            if route[ny][nx] == 0:
                route[ny][nx] = 1
                queue.append([time+1, ny, nx])
            elif route[ny][nx] == 2:
                last_time = time + n - ny + m - nx - 1
                answer = min(answer, last_time)

print('Fail' if t < answer else answer)