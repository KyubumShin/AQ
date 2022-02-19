import sys, heapq
from collections import defaultdict
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
infos = defaultdict(list)
answer = 0
for _ in range(n):
    line = input().split()
    name = line[1]
    if line[0] == '1':
        info = map(lambda x: -int(x), line[3:])
        infos[name].extend(info)
        heapq.heapify(infos[name])
    else:
        count = min(int(line[2]), len(infos[name]))
        for _ in range(count):
            answer -= heapq.heappop(infos[name])
print(answer)