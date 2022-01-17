import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
answer = []
n = int(input())
apt_map = []
for i in range(n):
    line = list(map(int, list(input().strip())))
    apt_map.append(line)
stack = []
num_house = 0
for i in range(n):
    for j in range(n):
        if apt_map[j][i] == 1:
            stack.append((i, j))
            apt_map[j][i] = 0
            num_house = 1
        while stack:
            cur = stack.pop()
            for k in range(4):
                nx = cur[0] + dx[k]
                ny = cur[1] + dy[k]
                if 0 <= nx < n and 0 <= ny < n:
                    if apt_map[ny][nx] == 1:
                        stack.append((nx, ny))
                        apt_map[ny][nx] = 0
                        num_house += 1
        if num_house != 0:
            answer.append(num_house)
            num_house = 0

print(len(answer))
for i in sorted(answer):
    print(i)