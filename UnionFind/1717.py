import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n, m = map(int, input().split())
rank = {i: 0 for i in range(n+1)}
parent = {i: i for i in range(n+1)}

print(parent)


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


for _ in range(m):
    i, a, b = map(int, input().split())
    if i == 0:
        union(a, b)
    else:
        pa, pb = find(a), find(b)
        if pa == pb:
            print("YES")
        else:
            print("NO")