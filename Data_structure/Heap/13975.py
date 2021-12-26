import sys
import heapq
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    k = int(input())
    num = list(map(int, input().split()))
    heapq.heapify(num)
    answer = 0
    while len(num) > 1:
        fst = heapq.heappop(num)
        snd = heapq.heappop(num)
        combine = fst + snd
        answer += combine
        print(combine)
        heapq.heappush(num, combine)
    print(num)
    print(answer)
