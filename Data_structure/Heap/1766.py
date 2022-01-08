import sys
import heapq
sys.stdin = open('input.txt')
input = sys.stdin.readline

n, m = map(int, input().split())
heap = []
route = [[] for _ in range(n+1)]
prev_q = [0 for _ in range(n+1)]
answer = []
for _ in range(m):
    f, s = map(int, input().split())
    route[f].append(s)
    prev_q[s] += 1

for i in range(1, n+1):
    if prev_q[i] == 0:
        heapq.heappush(heap, i)

while heap:
    cur = heapq.heappop(heap)
    answer.append(cur)
    for i in route[cur]:
        prev_q[i] -= 1
        if prev_q[i] == 0:
            heapq.heappush(heap, i)

print(' '.join(map(str, answer)))
