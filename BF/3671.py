import sys
from itertools import permutations
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
MAX = 10000000


def is_prime():
    prime = [0, 0] + [1] * MAX
    for k in range(2, 3164):
        if prime[k] == 1:
            for j in range(k*2, MAX, k):
                prime[j] = 0
    return prime


prime = is_prime()
for _ in range(n):
    count = 0
    nums = input().strip()
    visit = [0] * (int(''.join(sorted(nums, reverse=True))) + 1)
    for i in range(1, len(nums) + 1):
        for comb in permutations(sorted(nums), i):
            num = int(''.join(comb))
            if visit[num] == 0:
                visit[num] = 1
                if prime[num] == 1:
                    count += 1
    print(count)
