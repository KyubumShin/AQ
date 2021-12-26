import sys, heapq
sys.stdin = open('input.txt')
input = sys.stdin.readline
n, k = map(int, input().split())
c_id = [list(map(int, input().split())) for _ in range(n)]
heap = []
answer = []
for i in range(k):
    heapq.heappush(heap, [0, i])

for i in range(n):
    t, c_n = heapq.heappop(heap)
    heapq.heappush(heap, [t+c_id[i][1], c_n])
    answer.append([t+c_id[i][1], -c_n, i])

print(sum([(i+1) * c_id[data[2]][0] for i, data in enumerate(sorted(answer))]))
