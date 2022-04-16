import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    nn = int(input())
    nl = int(input())
    route = [[] for _ in range(nn+1)]
    for _ in range(nl):
        a, b = map(int, input().split())
        route[a].append(b)
        route[b].append(a)

    queue = deque([1])
    visit = [0] * (nn+1)
    visit[1] = 1
    flag = True

    #dfs
    while queue and flag:
        node = queue.popleft()
        count = 0
        for i in route[node]:
            if visit[i] == 1:
                count += 1
                if count > 1:
                    flag = False
                    break
            else:
                queue.append(i)
                visit[i] = 1
    print("tree" if flag and sum(visit) == nn else "graph")

