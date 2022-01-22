import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

def union(v, u):
    v_p = find(v)
    u_p = find(u)
    if v_p == u_p:
        return
    if rank[v_p] > rank[u_p]:
        parent[u_p] = v_p
    else:
        parent[v_p] = u_p
        if rank[u_p] == rank[v_p]:
            rank[u_p] += 1


def find(node):
    if parent[node] == node:
        return node
    parent[node] = find(parent[node])
    return parent[node]


if __name__ == '__main__':
    n = int(input())
    parent = [i for i in range(n+1)]
    rank = [0] * (n+1)
    for i in range(n-2):
        v, u = map(int, input().split())
        union(v, u)
    parent1 = find(1)
    print(parent)
    for i in range(2, n+1):
        if parent1 != find(i):
            print(parent1, i)
            break
    print(parent)
