import sys
from collections import defaultdict
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
s = input().strip()

right = 0
left = 0
check = defaultdict(int)
leng = 1
max_leng = 1
check[s[0]] = 1
while left < len(s):
    if len(check.keys()) <= n:
        max_leng = max(max_leng, leng)
        left += 1
        leng += 1
        if left >= len(s):
            break
        check[s[left]] += 1
    elif len(check.keys()) > n:
        check[s[right]] -= 1
        if check[s[right]] == 0:
            del check[s[right]]
        right += 1
        leng -= 1

print(max_leng)