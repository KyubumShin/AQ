import sys
import heapq
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
array = []
for _ in range(n):
    x = int(input())
    if x == 0:
        if len(array) == 0:
            print(0)
        else:
            abs_x, x = heapq.heappop(array)
            print(x)
    else:
        heapq.heappush(array, [abs(x), x])
