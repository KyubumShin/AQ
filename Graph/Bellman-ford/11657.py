import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

INF = int(5e9)
n, m = map(int, input().split())
route = {i: {} for i in range(1, n+1)}
for _ in range(m):
    a, b, c = map(int, input().split())
    if route[a].get(b):
        route[a][b] = min(c, route[a][b])
    else:
        route[a][b] = c
dist = [INF] * (n+1)


def bellman_ford(start):
    dist[start] = 0
    for i in range(n):
        for node in range(1, n+1):
            for next_node, cost in route[node].items():
                if dist[node] != INF and dist[next_node] > dist[node] + cost:
                    dist[next_node] = dist[node] + cost
                    if i == n-1:
                        return True
    return False


ret = bellman_ford(1)
if ret:
    print(-1)
else:
    for i in range(2, n+1):
        print(dist[i] if dist[i] != INF else -1)



