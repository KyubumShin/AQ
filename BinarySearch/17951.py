import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n, k = map(int, input().split())
problems = list(map(int, input().split()))

start = 0
end = sum(problems) + 1
while start+1 < end:
    mid = (start + end) // 2
    count = 0
    temp = 0
    for i in range(n):
        temp += problems[i]
        if temp >= mid:
            count += 1
            temp = 0
    if count >= k:
        start = mid
    else:
        end = mid
print(start)
