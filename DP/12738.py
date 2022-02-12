import sys, bisect
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
nums.reverse()
dp = [-1 * nums[0]]
for i in nums[1:]:
    if -1 * i > dp[-1]:
        dp.append(-i)
    else:
        idx = bisect.bisect_left(dp, -i)
        dp[idx] = -i
print(len(dp))
print(*list(map(lambda x: x*-1, reversed(dp))))
