import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline


def swan_bfs(swan_q: deque):
    global swan_other
    ret_q = deque()
    while swan_q:
        cur = swan_q.popleft()
        for i in range(4):
            nx = cur[1] + dx[i]
            ny = cur[0] + dy[i]
            if 0 <= nx < c and 0 <= ny < r:
                if ny == swan_other[0] and nx == swan_other[1]:
                    return time
                elif visit[ny][nx] == 1:
                    continue
                elif table[ny][nx] == '.':
                    visit[ny][nx] = 1
                    swan_q.append([ny, nx])
                elif table[ny][nx] == 0:
                    ret_q.append(cur)
    return ret_q


def melting_ice(ice_q: deque, first: bool):
    ret_q = deque()
    while ice_q:
        cur = ice_q.popleft()
        for i in range(4):
            nx = cur[1] + dx[i]
            ny = cur[0] + dy[i]
            if 0 <= nx < c and 0 <= ny < r:
                if first:
                    if table[ny][nx] == 1:
                        ret_q.append(cur)
                        break
                else:
                    if [ny, nx] in ret_q:
                        continue
                    if table[ny][nx] == 'X':
                        ret_q.append([ny, nx])
    for y, x in ret_q:
        table[y][x] = 1
    return ret_q


def main():
    global time
    swan = deque()
    ice = deque()
    for i in range(r):
        lst = list(input().strip())
        for j in range(len(lst)):
            if lst[j] == 'X':
                ice.append([i, j])
            elif lst[j] == 'L':
                swan.append([i, j])
            lst[j] = '.'
        table.append(lst)
    first = True
    while isinstance(swan, deque) and time < 5:
        swan = swan_bfs(swan)
        ice = melting_ice(ice, first)
        first = False
        time += 1
    else:
        print(swan)


if __name__ == "__main__":
    r, c = map(int, input().split())
    obj = {'.': 1, 'L': 2, 'X': 0}
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    table = []
    visit = [[0] * c for _ in range(r)]
    time = 0
    main()
