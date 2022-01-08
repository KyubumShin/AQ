import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

def union_1(v, u):
    v_p = find_1(v)
    u_p = find_1(u)
    if rank[v_p] > rank[u_p]:
        parent[u_p] = v_p
    else:
        parent[v_p] = u_p
        if rank[u_p] == rank[v_p]:
            rank[u_p] += 1

def find_1(node):
    if parent[node] == node:
        return node
    parent[node] = find_1(parent[node])
    return parent[node]

n, m = map(int, input().split())
parent = [i for i in range(n)]
rank = [0] * n
for i in range(1, m+1):
    u, v = map(int, input().split())
    u_p = find_1(u)
    v_p = find_1(v)
    if v_p == u_p:
        print(i)
        break
    union_1(v, u)
else:
    print(0)
