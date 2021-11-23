import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
row = []
col = []
for _ in range(n):
    r, c = list(map(int, input().split()))
    row.append(r)
    col.append(c)

dp = [[0 for _ in range(n)] for _ in range(n)]
for i in range(1, n):
    for start in range(0, n - i):
        end = start + i
        if start + 1 == end:
            dp[start][end] = row[start] * col[start] * col[end]
        else:
            dp[start][end] = 1 << 31
            for k in range(start, end):
                dp[start][end] = min(dp[start][end], dp[start][k] + dp[k+1][end] + row[start] * col[k] * col[end])
print(dp[0][-1])