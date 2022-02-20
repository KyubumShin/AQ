import sys
sys.setrecursionlimit(int(1e5))
sys.stdin = open('input.txt')
input = sys.stdin.readline
length = 16

n = int(input())
route = dict()
graph = [[] for _ in range(n+1)]
l = [0] * (n+1)
d = [0] * (n+1)
c = [0] * (n+1)
parent = [0] * (n+1)

for _ in range(n-1):
    f, s, length = map(int, input().split())
    route[(f, s)] = route[(s, f)] = length
    graph[f].append(s)
    graph[s].append(f)


def dfs(x, depth):
    c[x] = True
    d[x] = depth
    for y in graph[x]:
        if c[y]:
            continue
        parent[y] = x
        l[y] += l[x] + route[(x, y)]
        dfs(y, depth+1)


def lca(a, b):
    while d[a] != d[b]:
        if d[a] > d[b]:
            a = parent[a]
        else:
            b = parent[b]
    while a != b:
        a = parent[a]
        b = parent[b]
    return a


dfs(1, 0)

m = int(input())

for _ in range(m):
    a, b = map(int, input().split())
    print(l[a] + l[b] - 2 * l[lca(a, b)])
