import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline

def is_prime():
    prime_list = [True] * 10000
    for i in range(2, 100):
        if not prime_list[i]:
            continue
        for j in range(i*2, 10000, i):
            prime_list[j] = False

    return prime_list

n = int(input())
prime = is_prime()

for _ in range(n):
    A, B = map(int, input().split())
    queue = deque()
    visit = [False for _ in range(10000)]
    queue.append([A, 0])
    while queue:
        cur, cnt = queue.popleft()
        if cur == B:
            print(cnt)
            break
        str_cur = str(cur)
        for i in range(4):
            for j in range(10):
                n_cur = int(str_cur[:i] + str(j) + str_cur[i+1:])
                if not visit[n_cur] and prime[n_cur] and n_cur >= 1000:
                    visit[n_cur] = True
                    queue.append([n_cur, cnt+1])
    else:
        print("Impossible")