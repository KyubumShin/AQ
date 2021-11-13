import sys
from itertools import product, compress
sys.stdin = open('input.txt')
input = sys.stdin.readline
n = int(input())
food = []

for _ in range(n):
    s, b = map(int, input().split())
    food.append((s, b))

food_use = list(product(range(2),repeat=n))
max_diff = float('inf')
for selector in food_use[1:]:
    foods_used = compress(food, selector)
    total_s = 1
    total_b = 0
    for s, b in foods_used:
        total_s *= s
        total_b += b
    max_diff = min(max_diff, abs(total_s-total_b))
print(max_diff)
