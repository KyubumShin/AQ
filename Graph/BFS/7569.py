import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dh = [0, 0, 0, 0, 1, -1]
cnt = 0


def tomato_bfs(queue: deque) -> deque:
    global cnt
    ret_q = deque()
    while queue:
        c_h, c_y, c_x = queue.popleft()
        for i in range(6):
            nx = c_x + dx[i]
            ny = c_y + dy[i]
            nh = c_h + dh[i]
            if 0 <= nx < m and 0 <= ny < n and 0 <= nh < h:
                if tomato_box[nh][ny][nx] == 0:
                    ret_q.append([nh, ny, nx])
                    tomato_box[nh][ny][nx] = 1
    cnt += 1
    return ret_q

def check_tomato():
    for k in range(h):
        for j in range(n):
            if 0 in tomato_box[k][j]:
                return False
    return True


m, n, h = map(int, input().split())
tomato_box = []
tomato_queue = deque()
for k in range(h):
    temp = []
    for y in range(n):
        line = list(map(int, input().split()))
        for x in range(m):
            if line[x] == 1:
                tomato_queue.append([k, y, x])
        temp.append(line)
    tomato_box.append(temp)
while tomato_queue:
    tomato_queue = tomato_bfs(tomato_queue)
    print(cnt, '#' * 20)
    print(tomato_queue)
    for i in range(h):
        for j in range(n):
            print(*tomato_box[i][j])
if check_tomato():
    print(cnt-1)
else:
    print(-1)


