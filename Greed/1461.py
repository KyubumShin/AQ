import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n, m = map(int, input().split())
book_p = list(map(int, input().split()))
p_p, m_p = [], []
for i in book_p:
    if i < 0:
        m_p.append(-i)
    else:
        p_p.append(i)
m_p.sort(reverse=True)
p_p.sort(reverse=True)
dist = []
for i in range(len(m_p)//m):
    dist.append(m_p[m*i])
if len(m_p) % m != 0:
    dist.append(m_p[len(m_p)//m*m])

for i in range(len(p_p)//m):
    dist.append(p_p[m*i])
if len(p_p) % m != 0:
    dist.append(p_p[len(p_p)//m*m])

dist.sort()
answer = dist.pop()
answer += sum(dist)*2
print(answer)
