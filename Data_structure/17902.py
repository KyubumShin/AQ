import sys
from collections import defaultdict, Counter
sys.stdin = open('input.txt')
input = sys.stdin.readline

d = [-1, 0, 1]
h, w, n = map(int, input().split())
dic = defaultdict(int)
for _ in range(n):
    y, x = map(int, input().split())
    for i in range(3):
        for j in range(3):
            nx = x + d[i]
            ny = y + d[j]
            if 1< nx <w and 1< ny <h:
                dic[f"h{ny}w{nx}"] += 1
nums = Counter(dic.values())
print((h-2)*(w-2)-sum(nums.values()))
for i in range(1, 10):
    print(nums[i])
