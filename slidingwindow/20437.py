import sys
import string
from collections import defaultdict
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    max_l = 0
    min_l = 10001
    str_list = defaultdict(list)
    w = input().strip()
    k = int(input())
    for i, s in enumerate(w):
        str_list[s].append(i)
    for alpha_list in str_list.values():
        if len(alpha_list) >= k:
            for i in range(len(alpha_list)-k+1):
                max_l = max(max_l, alpha_list[i+k-1]-alpha_list[i]+1)
                min_l = min(min_l, alpha_list[i+k-1]-alpha_list[i]+1)
    if max_l == 0 and min_l == 10001:
        print(-1)
    else:
        print(min_l, max_l)
