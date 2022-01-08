import sys
import heapq
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
heap = []
for _ in range(n):
    i = int(input())
    if i == 0:
        if len(heap) > 0:
            print(heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap, i)
