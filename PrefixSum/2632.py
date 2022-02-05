import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

o = int(input())
m, n = map(int, input().split())
m_pizza = [int(input()) for _ in range(m)]
n_pizza = [int(input()) for _ in range(n)]

m_sum = [0] * (o+1)
n_sum = [0] * (o+1)
m_sum[0] = 1
n_sum[0] = 1

for i in range(len(m_pizza)):
    s = 0
    for j in range(len(m_pizza)):
        s += m_pizza[(i+j) % m]
        if s > o:
            break
        else:
            m_sum[s] += 1
for i in range(len(n_pizza)):
    s = 0
    for j in range(len(n_pizza)):
        s += n_pizza[(i+j) % n]
        if s > o:
            break
        else:
            n_sum[s] += 1

if sum(m_pizza) <= o:
    m_sum[sum(m_pizza)] += 1
if sum(n_pizza) <= o:
    n_sum[sum(n_pizza)] += 1

answer = 0
for i in range(o+1):
    answer += (m_sum[i] * n_sum[o-i])
print(answer)
