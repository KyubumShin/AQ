import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

p = []
for _ in range(3):
    p.extend(list(input().split()))
p = ''.join(p)
p = p.replace('0', '9')
p_0 = p.index('9')
queue = deque([])
queue.append([0, p_0, p])
visit = set([p])
while queue:
    cur, index, p = queue.popleft()
    if p == '123456789':
        print(cur)
        break
    x = index % 3
    y = index // 3
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < 3 and 0 <= ny < 3:
            k = nx + ny*3
            new_p = list(p)
            new_p[k], new_p[index] = new_p[index], new_p[k]
            new_p = ''.join(new_p)
            if new_p not in visit:
                visit.add(new_p)
                queue.append([cur+1, k ,new_p])
else:
    print(-1)
