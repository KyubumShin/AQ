import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n, c = map(int, input().split())
house = []
for _ in range(n):
    house.append(int(input()))
house.sort()

start = 1
end = house[-1] - house[0]
answer = 0

while start <= end:
    mid = (start + end) // 2
    count = 1
    cur = house[0]
    for i in range(1, len(house)):
        if house[i] >= cur + mid:
            count += 1
            cur = house[i]

    if count >= c:
        answer = mid
        start = mid + 1
    else:
        end = mid - 1

print(answer)
