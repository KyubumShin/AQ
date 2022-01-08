import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

def union(v, u):
    v_p = find_1(v)
    u_p = find_1(u)
    if v_p != u_p:
        parent[v_p] = u_p
        cnt[u_p] += cnt[v_p]
    print(cnt[u_p])

def find_1(node):
    if parent[node] == node:
        return node
    parent[node] = find_1(parent[node])
    return parent[node]

n = int(input())
for _ in range(n):
    f = int(input())
    parent, cnt = {}, {}
    for _ in range(f):
        u, v = input().split()
        if not parent.get(u):
            parent[u] = u
            cnt[u] = 1
        if not parent.get(v):
            parent[v] = v
            cnt[v] = 1
        union(v, u)

