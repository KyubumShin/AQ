import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
stack = []
answer = 0
for _ in range(n):
    print(stack, answer)
    x, y = map(int, input().split())
    while stack and stack[-1] > y:
        answer += 1
        stack.pop()
    if stack and stack[-1] == y:
        continue
    stack.append(y)
print(stack, answer)
while stack:
    answer += 1 if stack[-1] != 0 else 0
    stack.pop()
print(answer)
