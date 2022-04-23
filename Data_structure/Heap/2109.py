import sys
import heapq
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
l = [list(map(int, input().split())) for _ in range(n)]

l.sort(key=lambda x: x[1])
print(l)
heap=[]
for i in l:
    heapq.heappush(heap, i[0])
    if len(heap) > i[1]:
        heapq.heappop(heap)

print(sum(heap))