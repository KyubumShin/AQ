import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, S, P = map(int,input().split())
route = [[] for _ in range(N+1)]
for _ in range(N-1):
    v, e = map(int, input().split())
    route[v].append(e)
    route[e].append(v)
print(route)

visit = [0] * (N+1)
queue = deque([])
queue.append([P, 0])
count = 0
answer = 0
while queue:
    cur, length = queue.popleft()
    visit[cur] = 1
    for ice in route[cur]:
        if visit[ice] == 1:
            continue
        if ice <= S:
            count += 1
            answer += length+1
            if count == 2:
                break
        queue.append([ice, length+1])
    if count == 2:
        break
print(N - (answer + 1))

