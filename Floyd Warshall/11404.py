import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline
n = int(input())
m = int(input())
route = [[float('inf') for _ in range(n)] for _ in range(n)]
for i in range(n):
    route[i][i] = 0
for _ in range(m):
    s, e, c = map(int, input().split())
    if route[s-1][e-1] > c:
        route[s-1][e-1] = c
# 플로이드 와샬

for k in range(n):
    for i in range(n):
        for j in range(n):
            if route[i][k] + route[k][j] < route[i][j]:
                route[i][j] = route[i][k] + route[k][j]

for i in range(n):
    print(" ".join(map(str, map(lambda x: 0 if x == float('inf') else x, route[i]))))

