import sys
from collections import defaultdict
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
array = []
answer = [0] * n
color = defaultdict(int)
for i in range(n):
    c, s = map(int, input().split())
    array.append([s, c, i])

array.sort()
total = 0
same = defaultdict(int)
past_s = 0
for s, c, i in array:
    total += s
    color[c] += s
    if past_s == s:
        same[c] += 1
        print(same)
        answer[i] = total - color[c] - past_s*(sum(same.values()) - same[c])
    else:
        answer[i] = total - color[c]
        past_s = s
        same = defaultdict(int)
        same[c] += 1

for i in answer:
    print(i)