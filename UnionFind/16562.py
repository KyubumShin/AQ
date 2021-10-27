import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
n, m, k = map(int, input().split())
rank = {i: 0 for i in range(n+1)}
parent = {i: i for i in range(1, n+1)}
friend_tax = [0] + list(map(int, input().split()))


def find(node):
    if parent[node] == node:
        return node
    parent[node] = find(parent[node])
    return parent[node]


def union(v, u):
    v_p = find(v)
    u_p = find(u)
    if friend_tax[v_p] > friend_tax[u_p]:
        parent[u_p] = v_p
        friend_tax[v_p] = min(friend_tax[u_p], friend_tax[v_p])
    else:
        parent[v_p] = u_p
        friend_tax[u_p] = min(friend_tax[u_p], friend_tax[v_p])


for _ in range(m):
    v, w = map(int, input().split())
    union(v, w)

fake_friend = set()
require_tax = 0

for i in range(1, n+1):
    p = find(i)
    if p not in fake_friend:
        fake_friend.add(p)
        require_tax += friend_tax[p]

if require_tax > k:
    print("Oh no")
else:
    print(require_tax)
