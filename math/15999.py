# 분할정복을 이용한 거듭제곱
import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

n, m = map(int, input().split())
dic = {'W': 0, 'B': 1}
grid = [list(map(lambda x: dic[x], input().strip())) for _ in range(n)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
count = 0
for i in range(n):
    for j in range(m):
        for k in range(4):
            nx = j + dx[k]
            ny = i + dy[k]
            if 0 <= nx < m and 0 <= ny < n:
                if grid[i][j] != grid[ny][nx]:
                    count += 1
                    break

def f_pow(C, n):
    if n == 1:
        return C
    else:
        x = f_pow(C, n // 2)
        if n % 2 == 0:
            return x * x % 1000000007
        else:
            return x * x * C % 1000000007


print(f_pow(2, n * m - count))