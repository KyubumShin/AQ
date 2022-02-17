import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline


def topology_sort(tree, in_degree):
    ret = [1] * len(in_degree)
    queue = deque()
    for i in range(1, len(in_degree)):
        if in_degree[i] == 0:
            queue.append(i)
    while queue:
        cur = queue.popleft()
        for i in tree[cur]:
            in_degree[i] -= 1
            ret[i] = max(ret[i], ret[cur]+1)
            if in_degree[i] == 0:
                queue.append(i)
    return ret


n, m = map(int, input().split())
inDegree = [0] * (n+1)
build_tree = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    build_tree[a].append(b)
    inDegree[b] += 1
print(*topology_sort(build_tree, inDegree)[1:])
