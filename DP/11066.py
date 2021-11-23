import sys
import numpy as np
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    k = int(input())
    num = list(map(int, input().split()))
    dp = [[0] * k for _ in range(k)]
    for i in range(k - 1):
        dp[i][i + 1] = num[i] + num[i + 1]
        for j in range(i + 2, k):
            dp[i][j] = dp[i][j - 1] + num[j]

    for i in range(1, k):
        for start in range(k - i):
            end = start + i
            minimum = [dp[start][j] + dp[j+1][end] for j in range(start, end)]
            dp[start][end] += min(minimum)
    print(dp[0][-1])
