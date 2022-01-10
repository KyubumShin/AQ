import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline

r, c = map(int, input().split())
obj = {'.': 1, 'L': 2, 'X': 0}
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
table = []
swan = []
swan_other = []
swan_visit = [[0] * c for _ in range(r)]
ice = []
time = 0

for i in range(r):
    lst = list(map(lambda x: obj[x], list(input().strip())))
    for j in range(len(lst)):
        if lst[j] == 0:
            ice.append([i, j])
        elif lst[j] == 2:
            if not swan:
                swan.append([i, j])
            else:
                swan_other.append([i, j])
            lst[j] = 1
    table.append(lst)
print(table)
print(swan)
print(swan_other)
print(ice)


def swan_bfs(swan_q: deque):
    ret_q = deque()
    while swan_q:
        cur = swan_q.popleft()
        for i in range(4):
            nx = cur[1] + dx[i]
            ny = cur[0] + dy[i]
            if 0 <= nx < c and 0 <= ny < r:
                if swan_visit[ny][nx] == 1:
                    continue
                elif table[ny][nx] == 1:
                    swan_visit[ny][nx] = 1
                    swan_q.append([ny, nx])
                elif table[ny][nx] == 0:
                    ret_q.append(cur)
                elif [ny, nx] == swan_other:
                    return time
    return ret_q


print(swan_bfs(deque(swan)))

def ice_bfs(queue):
    pass



