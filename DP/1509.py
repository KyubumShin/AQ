import sys

sys.stdin = open('../input.txt')
input = sys.stdin.readline


def dp():
    nums_dp = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(0, n):
        for j in range(0, n-i):
            if i == 0:
                nums_dp[j][j+i] = 1
            elif nums[j] == nums[j+i]:
                if j+1 == j+i:
                    nums_dp[j][j+1] = 1
                elif nums_dp[j+1][j+i-1] == 1:
                    nums_dp[j][j+i] = 1
    return nums_dp

nums = input().strip()
n = len(nums)
dp_list = dp()
f = [2501] * n + [0]
f[0] = 1
for end in range(0, n):
    for start in range(0, end + 1):
        if dp_list[start][end] == 1:
            f[end] = min(f[end], f[start - 1] + 1)

print(f[-2])
