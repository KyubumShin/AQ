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
                    swan_q.append([ny, nx])
                elif table[ny][nx] == 'X':
                    ret_q.append([ny, nx])
                visit[ny][nx] = 1
    return ret_q


def melting_ice(water_q: deque):
    ret_q = deque()
    while water_q:
        cur = water_q.popleft()
        for i in range(4):
            nx = cur[1] + dx[i]
            ny = cur[0] + dy[i]
            if 0 <= nx < c and 0 <= ny < r:
                if table[ny][nx] == 'X':
                    ret_q.append([ny, nx])
                    table[ny][nx] = '.'
    return ret_q


def main():
    global time, swan_other
    swan = deque()
    water = deque()
    for i in range(r):
        lst = list(input().strip())
        for j in range(len(lst)):
            if lst[j] == 'L':
                swan.append([i, j])
                lst[j] = '.'
            elif lst[j] == 'L':
                water.append([i, j])
        table.append(lst)
    swan_other = swan.pop()
    while isinstance(swan, deque) and time < 5:
        swan = swan_bfs(swan)
        water = melting_ice(water)
        time += 1
    else:
        print(swan)


if __name__ == "__main__":
    r, c = map(int, input().split())
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    table = []
    visit = [[0] * c for _ in range(r)]
    time = 0
    main()
