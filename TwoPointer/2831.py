import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())

men_p, men_m = [], []
for man in map(int, input().split()):
    if man > 0:
        men_p.append(man)
    else:
        men_m.append(man)

women_p, women_m = [], []
for woman in map(int, input().split()):
    if woman > 0:
        women_p.append(woman)
    else:
        women_m.append(woman)


def cal_pair(ps, ms):
    ps = sorted(ps)
    ms = sorted(ms, reverse=True)
    p_i, m_i = 0, 0
    cnt = 0
    while len(ps) > p_i:
        while len(ms) > m_i:
            if ps[p_i] + ms[m_i] < 0:
                m_i += 1
                cnt += 1
                break
            else:
                m_i += 1
        if m_i == len(ms):
            break
        p_i += 1
    return cnt


print(cal_pair(women_p, men_m) + cal_pair(men_p, women_m))