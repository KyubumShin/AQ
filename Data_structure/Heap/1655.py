import sys
import heapq

sys.stdin = open('input.txt')
input = sys.stdin.readline
n = int(input())
max_heap = []
min_heap = []
for _ in range(n):
    num = int(input())
    if len(max_heap) == 0:
        heapq.heappush(max_heap, -num)
    else:
        if len(max_heap) == len(min_heap):
            heapq.heappush(max_heap, -num)
        else:
            heapq.heappush(min_heap, num)
        if min_heap[0] < -1 * max_heap[0]:
            a = -heapq.heappop(max_heap)
            b = heapq.heappop(min_heap)
            heapq.heappush(max_heap, -b)
            heapq.heappush(min_heap, a)
    print(-max_heap[0])
