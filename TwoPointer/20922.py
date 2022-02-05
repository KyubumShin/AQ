import sys
from collections import defaultdict
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, K = map(int, input().split())
nums = list(map(int, input().split()))
num_dict = defaultdict(int)
right, left = 0, 0
answer = 0
while left < N:
    num_dict[nums[left]] += 1
    if num_dict[nums[left]] > K:
        answer = max(answer, sum(num_dict.values())-1)
        while num_dict[nums[left]] > K:
            num_dict[nums[right]] -= 1
            right += 1
    left += 1
else:
    answer = max(answer, sum(num_dict.values()))
print(answer)