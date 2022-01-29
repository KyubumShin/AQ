import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, P = map(int, input().split())
stack = {i: [0] for i in range(1, N+1)}
answer = 0

for i in range(N):
    line, p = map(int, input().split())
    if stack[line][-1] == p:
        continue
    elif stack[line][-1] < p:
        stack[line].append(p)
        answer += 1
    else:
        while stack[line][-1] > p:
            stack[line].pop()
            answer += 1
        if stack[line][-1] != p:
            answer += 1
            stack[line].append(p)
print(answer)
