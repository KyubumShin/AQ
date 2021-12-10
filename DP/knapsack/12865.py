import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, K = map(int, input().split())
item = []
for _ in range(N):
    item.append(list(map(int, input().split())))
# dp = [[0] * (K+1) for _ in range(N+1)]
# for i in range(1, N+1):
#     w, v = item[i-1]
#     for j in range(1, K+1):
#         if j < w:
#             dp[i][j] = dp[i-1][j]
#         else:
#             dp[i][j] = max(v + dp[i-1][j-w], dp[i-1][j])
# print(dp[-1][-1])

# 최적화
dp = [0] * (K+1)
item.sort()
print(item)
for w, v in item:
    for j in range(K, w-1, -1):
        dp[j] = max(v + dp[j-w], dp[j])
print(dp[-1])
