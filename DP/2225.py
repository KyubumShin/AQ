import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, K = map(int, input().split())

dp = [1] + [0] * N
mod = 1e9

for _ in range(1, K+1):
    for j in range(1, N+1):
        dp[j] = (dp[j] + dp[j-1]) % mod
print(int(dp[-1]))