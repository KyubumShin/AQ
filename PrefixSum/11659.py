import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
prefix_sum = [0]
sums = 0
for i in nums:
    sums += i
    prefix_sum.append(sums)

for _ in range(m):
    i, j = map(int, input().split())
    print(prefix_sum[j] - prefix_sum[i-1])
