import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n, k = map(int, input().split())
nums = list(map(int, input().split()))
left, right, _sum = 0, 0, 0
dp = [0] * (n+1)

while left <= right <= n:
    if _sum >= k:
        while _sum >= k:
            dp[right] = max(dp[right], dp[left] + _sum - k)
            _sum -= nums[left]
            left += 1
    else:
        dp[right] = max(dp[right], dp[right-1])
        if right == n:
            break
        _sum += nums[right]
        right += 1
print(dp[n])