import sys
import heapq
sys.stdin = open('input.txt')
input = sys.stdin.readline
INF = int(1e9)


def dijkstra(start):
    distance = [INF] * (n + 1)
    distance[start] = 0
    queue = []
    heapq.heappush(queue, (0, start))
    while queue:
        dis, current = heapq.heappop(queue)
        if distance[current] < dis:
            continue
        for next_pos, l in dist[current]:
            next_dis = l + dis
            if next_dis < distance[next_pos]:
                distance[next_pos] = next_dis
                heapq.heappush(queue, (next_dis, next_pos))
    return distance


T = int(input())
for _ in range(T):
    n, m, k = map(int, input().split())
    s, g, h = map(int, input().split())
    dist = [[] for i in range(n+1)]
    for _ in range(m):
        x, y, d = map(int, input().split())
        dist[x].append((y, d))
        dist[y].append((x, d))

    dest = []
    for _ in range(k):
        dest.append(int(input()))
    first = dijkstra(s)
    g_dijk = dijkstra(g)
    h_dijk = dijkstra(h)
    answer = []
    for b in dest:
        if first[g] + g_dijk[h] + h_dijk[b] == first[b] or first[h] + h_dijk[g] + g_dijk[b] == first[b]:
            answer.append(b)
    answer.sort()
    for f in answer:
        print(f, end=' ')
    print()

