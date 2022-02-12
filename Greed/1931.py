import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
time = []
for _ in range(n):
    time.append(list(map(int, input().split())))
time.sort(key=lambda x: (x[1], x[0]))
print(time)
cur = 0
answer = 0
for s, e in time:
    if cur <= s:
        cur = e
        answer += 1
print(answer)