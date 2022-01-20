import sys
import heapq
sys.stdin = open('input.txt')
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dijkstra():
    distance = [float('inf')] * (n * n)
    distance[0] = rupee_map[0][0]
    queue = []
    heapq.heappush(queue, [rupee_map[0][0], 0, 0])
    while queue:
        dis, y, x = heapq.heappop(queue)
        current = y * n + x
        if distance[current] < dis:
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            next_pos = ny * n + nx
            if 0 <= ny < n and 0 <= nx < n:
                next_dis = dis + rupee_map[ny][nx]
                if next_dis < distance[next_pos]:
                    distance[next_pos] = next_dis
                    heapq.heappush(queue, (next_dis, ny, nx))
    print(distance)
    print(f'Problem {p_num}: {distance[-1]}')

p_num = 1
while True:
    n = int(input())
    if n == 0:
        break
    rupee_map = [list(map(int, input().split())) for _ in range(n)]
    dijkstra()
    p_num += 1

