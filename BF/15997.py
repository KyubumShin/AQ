import sys
from itertools import product
from collections import Counter
sys.stdin = open('input.txt')
input = sys.stdin.readline

country = input().split()
play_lists = []
c2num = dict()
for i, c in enumerate(country):
    c2num[c] = i

point = {i: 0 for i in country}
for _ in range(6):
    F, S, F_win, draw, S_win = input().split()
    if F_win == "1.0":
        point[F] += 3
    elif draw == "1.0":
        point[F] += 1
        point[S] += 1
    elif S_win == "1.0":
        point[S] += 3
    else:
        play_lists.append([F, S, float(F_win), float(draw), float(S_win)])


def cal_rank(points, cur_per):
    cnt = 0
    c_s = sorted(Counter(points.values()).items(), reverse=True)
    for num, count in c_s:
        if cnt + count > 2:
            if cnt < 2:
                for name, p in points.items():
                    if p == num:
                        answer[name] += (2-cnt) * (cur_per/count)
            break
        else:
            cnt += count
            for key in points:
                if points[key] == num:
                    answer[key] += cur_per


answer = {i: 0.0 for i in country}
for per in product(range(3), repeat=len(play_lists)):
    temp_point = point.copy()
    percent = 1.0
    for n, play_list in zip(per, play_lists):
        if n == 0:
            temp_point[play_list[0]] += 3
        elif n == 1:
            temp_point[play_list[0]] += 1
            temp_point[play_list[1]] += 1
        else:
            temp_point[play_list[1]] += 3
        percent *= play_list[n+2]
    if percent == 0.0:
        continue
    cal_rank(temp_point, percent)

for i in point:
    print(answer[i])
