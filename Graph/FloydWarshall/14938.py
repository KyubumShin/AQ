import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

INF = float('inf')
n, m, r = map(int, input().split())
items = [0] + list(map(int, input().split()))
route = [[INF] * (n+1) for _ in range(n+1)]
for _ in range(r):
    a, b, length = map(int, input().split())
    route[a][b] = length
    route[b][a] = length

can_search = [[0 for _ in range(n+1)] for _ in range(n+1)]
for i in range(n+1):
    can_search[i][i] = 1

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if route[i][k] + route[k][j] < route[i][j]:
                route[i][j] = route[i][k] + route[k][j]
            if route[i][j] <= m:
                can_search[i][j] = 1

answer = 0
for line in can_search[1:]:
    answer = max(answer, sum(list(map(lambda a: a[0] * a[1], zip(line, items)))))
print(answer)