import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline


def topology_sort(tree, in_degree, is_possible):
    ret = [1] * len(in_degree)
    queue = deque()
    answer = []
    for i in range(1, len(in_degree)):
        if in_degree[i] == 0:
            queue.append(i)
    while queue:
        cur = queue.popleft()
        answer.append(cur)
        for i in tree[cur]:
            in_degree[i] -= 1
            ret[i] = max(ret[i], ret[cur]+1)
            if in_degree[i] == 0:
                queue.append(i)
            elif in_degree[i] < 0:
                is_possible = False
    return answer, is_possible

n = int(input())

for _ in range(n):
    n_t = int(input())
    in_degree = [0] * (n_t + 1)
    build_tree = [[] for _ in range(n_t + 1)]
    is_possible = True
    p_rank = list(map(int, input().split()))
    for i in range(len(p_rank)-1):
        for j in range(i+1, len(p_rank)):
            build_tree[p_rank[i]].append(p_rank[j])
            in_degree[p_rank[j]] += 1

    t = int(input())
    for i in range(t):
        c, p = map(int, input().split())
        if p in build_tree[c]:
            build_tree[c].remove(p)
            in_degree[c] += 1
            build_tree[p].append(c)
            in_degree[p] -= 1
        else:
            build_tree[p].remove(c)
            in_degree[p] += 1
            build_tree[c].append(p)
            in_degree[c] -= 1

    answer, is_possible = topology_sort(build_tree, in_degree, is_possible)
    if is_possible and len(answer) == n_t:
        print(*answer)
    else:
        print("IMPOSSIBLE")

