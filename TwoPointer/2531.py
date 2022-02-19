import sys
from collections import defaultdict
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, d, k, c = map(int, input().split())
sushi = []
for _ in range(N):
    s = int(input())
    sushi.append(s)

sushi = sushi+sushi
sushi_eat = defaultdict(int)
start = 0
end = k
sushi_eat[c] += 1

for i in range(end):
    sushi_eat[sushi[i]] += 1

answer = 0
for i in range(N):
    answer = max(answer, len(sushi_eat))
    sushi_eat[sushi[start]] -= 1
    if sushi_eat[sushi[start]] < 1:
        del(sushi_eat[sushi[start]])
    sushi_eat[sushi[end]] += 1
    start += 1
    end += 1

print(answer)