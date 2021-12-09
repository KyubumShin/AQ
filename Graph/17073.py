import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, W = map(int, input().split())
route = [[] for _ in range(N)]
visit = [0] * N
for _ in range(N-1):
    a, b = map(int, input().split())
    route[a-1].append(b-1)
    route[b-1].append(a-1)

# queue = deque([0])
# leaf_count = 0
# while queue:
#     node = queue.popleft()
#     visit[node] = 1
#     child_count = 0
#     for i in route[node]:
#         if visit[i] == 0:
#             if len(route[i]) == 1 and route[i][0] == node:
#                 leaf_count += 1
#             else:
#                 queue.append(i)
#
# print(W/leaf_count)

# edge수가 1인 node만 구해도 풀림
from collections import Counter
edge_sum = list(map(len, route))
print(W/Counter(edge_sum)[1])
