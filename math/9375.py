import sys
from collections import defaultdict
sys.stdin = open('input.txt')
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    dic = defaultdict(int)
    if n == 0:
        print(0)
        continue
    for _ in range(n):
        _, category = input().strip().split()
        dic[category] += 1
    answer = 1
    for i in dic.values():
        answer *= (i+1)
    print(answer-1)