import sys
sys.stdin = open('input.txt')
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

n = int(input())
nums = list(map(int, input().split()))
dp_list = dp()
m = int(input())
for _ in range(m):
    s, e = map(int, input().split())
    print(dp_list[s-1][e-1])



