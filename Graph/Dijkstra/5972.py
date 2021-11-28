import sys
import heapq
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M = map(int, input().split())
dist = [[] for i in range(N)]
distance = [0] + [float('inf')] * (N-1)

for _ in range(M):
    x, y, d = map(int, input().split())
    dist[x-1].append([y-1, d])
    dist[y-1].append([x-1, d])
# 다익스트라
queue = []
heapq.heappush(queue, [0, 0])
while queue:
    dis, current = heapq.heappop(queue)
    if distance[current] < dis:
        continue
    for next_pos, l in dist[current]:
        next_dis = l + dis
        if next_dis < distance[next_pos]:
            distance[next_pos] = next_dis
            queue.append((next_dis, next_pos))
print(distance)
