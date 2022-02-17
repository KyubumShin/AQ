import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline


def topology_sort(time, tree, inDegree, end):
    ret = [0] * len(inDegree)
    queue = deque()
    for i in range(1, len(inDegree)):
        if inDegree[i] == 0:
            queue.append(i)
            ret[i] = time[i]
    while queue:
        current = queue.popleft()
        for i in tree[current]:
            inDegree[i] -= 1
            ret[i] = max(ret[i], time[i] + ret[current])
            if inDegree[i] == 0:
                queue.append(i)
    return ret[end]


n = int(input())
for _ in range(n):
    m, k = map(int, input().split())
    D = [0] + list(map(int, input().split()))
    build_tree = [[] for _ in range(m+1)]
    inDegree = [0] * (k+1)
    for _ in range(k):
        c, p = map(int, input().split())
        build_tree[c].append(p)
        inDegree[p] += 1
    end = int(input())
    print(topology_sort(D, build_tree, inDegree, end))
