import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
m = int(input())

parent = [0] + [-1] * n  # -1로 부모노드를 초기화


def weight_find(node: int):
    if parent[node] < 0:  # 값이 음수면 부모노드
        return node
    parent[node] = weight_find(parent[node])
    return parent[node]


def weight_union(v, u):
    v_p = weight_find(v)
    u_p = weight_find(u)
    if v_p == u_p:
        return
    if parent[v_p] < parent[u_p]:  # 부모노드의 값이 음수이기 때문에 더 작으면 더 깊은 트리
        parent[v_p] += parent[u_p]
        parent[u_p] = v_p
    else:
        parent[u_p] += parent[v_p]
        parent[v_p] = u_p


for i in range(1, n+1):
    route = list(map(int, input().split()))
    for j in range(1, len(route)):
        if route[j-1] == 1:
            weight_union(i, j)

trip_route = list(map(int, input().split()))
result = weight_find(trip_route[0])
for i in trip_route:
    if weight_find(i) != result:
        print("NO")
        break
else:
    print("YES")
print(parent)
