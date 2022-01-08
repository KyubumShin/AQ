import sys, copy
from collections import deque
from itertools import combinations
sys.stdin = open('input.txt')
input = sys.stdin.readline

n, k = input().split()
n = list(n)
k = int(k)

queue = deque()
d = list(combinations(range(len(n)), 2))
queue.append((n, 0))

answer = []

def bfs():
    visit = [0] * 1000001
    ans = 0
    q_len = len(queue)
    while q_len > 0:
        cur, k_n = queue.popleft()
        for i, j in d:
            temp = copy.deepcopy(cur)
            temp[i], temp[j] = temp[j], temp[i]
            if temp[0] == '0':
                continue
            num = int(''.join(temp))
            if visit[num] == 0:
                visit[num] = 1
                ans = max(ans, num)
                queue.append((temp, k_n+1))
        q_len -= 1
    return ans

for i in range(k):
    ans = bfs()

print(ans if ans != 0 else -1)