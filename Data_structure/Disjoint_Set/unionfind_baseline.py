parent = {}
rank = {}


def find_base(node):
    if parent[node] == node:
        return node
    return find_base(parent[node])


def union(v, u):
    v_p = find_base(v)
    u_p = find_base(u)
    if v_p != u_p:
        parent[v_p] = u_p


# parent를 합치는 과정에서의 최적화
def find_1(node):
    if parent[node] == node:
        return node
    parent[node] = find_1(parent[node])
    return parent[node]


# rank를 이용한 최적화
def union_1(v, u):
    v_p = find_base(v)
    u_p = find_base(u)
    if rank[v_p] > rank[u_p]:
        parent[u_p] = v_p
    else:
        parent[v_p] = u_p
        if rank[u_p] == rank[v_p]:
            rank[u_p] += 1


# weight union find : rank를 안쓰고 깊이 최적화 시키는 방법
parent = {i: -1 for i in range(1, n + 1)}  # -1로 부모노드를 초기화


def weight_find(node: int):
    if parent[node] < 0:  # 값이 음수면 부모노드
        return node
    parent[node] = weight_find(parent[node])
    return parent[node]


def weight_union(v, u):
    v_p = weight_find(v)
    u_p = weight_find(u)
    if parent[v_p] < parent[u_p]:  # 부모노드의 값이 음수이기 때문에 더 작으면 더 깊은 트리
        parent[v_p] += parent[u_p]  #
        parent[u_p] = v_p
    else:
        parent[u_p] += parent[v_p]
        parent[v_p] = u_p
