import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
v, e = map(int, input().split())
edges = []
parent = dict()
rank = dict()
cnt = 0

for _ in range(e):
    a, b, w = map(int, input().split())
    edges.append([w,a,b])
edges.sort()
for i in range(1,v+1):
    parent[i] = i
    rank[i] = 0


def find(node):
    if parent[node] == node:
        return node
    return find(parent[node])


def union(v, u):
    v_p = find(v)
    u_p = find(u)
    if rank[v_p] > rank[u_p]:
        parent[u_p] = v_p
    else:
        parent[v_p] = u_p
        if rank[u_p] == rank[v_p]:
            rank[u_p] += 1


for edge in edges:
    w, v, u = edge
    if find(v) != find(u):
        union(v,u)
        cnt += w

print(cnt)
