# 12015 공통
import sys, bisect
input = sys.stdin.readline
n = int(input())
nums = list(map(int, input().split()))
dp = [nums[0]]
for i in nums[1:]:
    if i > dp[-1]:
        dp.append(i)
    else:
        idx = bisect.bisect_left(dp, i)
        dp[idx] = i
print(len(dp))
