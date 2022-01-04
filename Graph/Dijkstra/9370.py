import sys
import math
import heapq
sys.stdin = open('input.txt')
input = sys.stdin.readline

T = int(input())


def dijkstra(start):
    distance = [math.inf] * (n + 1)
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


for _ in range(T):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())
    dist = [[] for i in range(n+1)]
    for _ in range(m):
        x, y, d = map(int, input().split())
        dist[x].append([y, d])
        dist[y].append([x, d])
    dest = [int(input()) for _ in range(t)]
    answer = []
    length_s = dijkstra(s)
    length_g = dijkstra(g)
    length_h = dijkstra(h)
    for i in dest:
        if length_s[g] + length_g[h] + length_h[i] == length_s[i] or length_s[h] + length_g[i] + length_h[g] == length_s[i]:
            answer.append(i)
    for f in sorted(answer):
        print(f, end=' ')
    print()

