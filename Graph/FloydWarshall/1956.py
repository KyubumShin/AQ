import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
v, e = map(int, input().split())
INF = float('inf')
route = [[INF for _ in range(v)] for _ in range(v)]

for _ in range(e):
    s, e, c = map(int, input().split())
    if route[s-1][e-1] > c:
        route[s-1][e-1] = c

# 플로이드 와샬
for k in range(v):
    for i in range(v):
        for j in range(v):
            if route[i][k] + route[k][j] < route[i][j]:
                route[i][j] = route[i][k] + route[k][j]

answer = float('inf')
for i in range(v):
    for j in range(v):
        if route[i][j] < answer and route[j][i] < answer and i != j:
            answer = min(answer, route[i][i])

print(answer if answer is not INF else -1)
