import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
cnt = 0


def tomato_bfs(queue: deque) -> deque:
    global cnt
    ret_q = deque()
    while queue:
        c_y, c_x = queue.popleft()
        for i in range(6):
            nx = c_x + dx[i]
            ny = c_y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if tomato_box[ny][nx] == 0:
                    ret_q.append([ny, nx])
                    tomato_box[ny][nx] = 1
    cnt += 1
    return ret_q


def check_tomato():
    for j in range(n):
        if 0 in tomato_box[j]:
            return False
    return True


m, n = map(int, input().split())
tomato_box = []
tomato_queue = deque()
for y in range(n):
    line = list(map(int, input().split()))
    for x in range(m):
        if line[x] == 1:
            tomato_queue.append([y, x])
    tomato_box.append(line)

while tomato_queue:
    tomato_queue = tomato_bfs(tomato_queue)
    print(cnt, '#' * 20)
    print(tomato_queue)
    for i in range(n):
        print(*tomato_box[i])
if check_tomato():
    print(cnt-1)
else:
    print(-1)