import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    k = int(input())
    num = list(map(int, input().split()))
    print(sorted(num))

# 1 3 3 4 4 5 5 5 14 17 21 21 32 35 98