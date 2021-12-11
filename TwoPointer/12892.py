import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, D = map(int, input().split())
present_list = [list(map(int, input().split())) for _ in range(N)]
present_list.sort()
print(present_list)
right, left = 0, 1
answer = present_list[0][1]
sum_v = present_list[0][1]
cur_min = present_list[0][0]
while left < len(present_list):
    p, v = present_list[left]
    if p - cur_min < D:
        sum_v += v
        left += 1
    else:
        sum_v += v
        left += 1
        while True:
            cur_min, v = present_list[right]
            if p - cur_min >= D:
                sum_v -= v
                right += 1
            else:
                break
    answer = max(sum_v, answer)
print(answer)
