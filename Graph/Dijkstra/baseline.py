import heapq

def dijkstra(start):
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