import sys
import heapq
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M = map(int, input().split())
dist = [[] for i in range(N+1)]
for _ in range(M):
    x, y, d = map(int, input().split())
    dist[x].append([y, d])
    dist[y].append([x, d])
v1, v2 = map(int, input().split())
print(dist)

def dijkstra(start):
    distance = [float('inf')] * (N+1)
    distance[start] = 0
    queue = []
    heapq.heappush(queue, [0, start])
    while queue:
        dis, current = heapq.heappop(queue)
        if distance[current] < dis:
            continue
        for next_pos, l in dist[current]:
            next_dis = l + dis
            if next_dis < distance[next_pos]:
                distance[next_pos] = next_dis
                queue.append((next_dis, next_pos))
    return distance


route_v1 = dijkstra(v1)
route_v2 = dijkstra(v2)

answer = min(route_v1[1]+route_v1[v2]+route_v2[-1], route_v2[1]+route_v2[v1]+route_v1[-1])
print(answer if answer < 200000000 else -1)
