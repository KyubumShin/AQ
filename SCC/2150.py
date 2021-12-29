import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

v, e = map(int, input().split())

stack = []
low = [-1] * (v+1)
ids = [-1] * (v+1)
visited = [0] * (v+1)
_id = 1
ret = []
route = [[] for _ in range(v+1)]


for _ in range(e):
    a, b = map(int, input().split())
    route[a].append(b)


def dfs(x, low, ids, visited, stack):
    global _id
    ids[x] = _id
    low[x] = _id
    _id += 1
    visited[x] = 1
    stack.append(x)

    for i in route[x]:
        if ids[i] == -1:
            dfs(i, low, ids, visited, stack)
            low[x] = min(low[x], low[i])
        elif visited[i] == 1:
            low[x] = min(low[x], ids[i])
    scc = []
    w = -1
    if low[x] == ids[x]:
        while w != x:
            w = stack.pop()
            scc.append(w)
            visited[w] = -1
        ret.append(sorted(scc))

for i in range(1, v+1):
    if ids[i] == -1:
        dfs(i, low, ids, visited, stack)
print(len(ret))
for i in sorted(ret):
    print(*i, -1)

