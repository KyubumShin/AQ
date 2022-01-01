import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())

a = [False, False] + [True] * (n-1)
for i in range(2, n+1):
    if a[i]:
        for j in range(2*i, n+1, i):
            a[j] = False

if n < 8:
    print(-1)
else:
    if n % 2 == 0:
        n -= 4
        answer = [2, 2]
    elif n % 2 == 1:
        n -= 5
        answer = [2, 3]

    for i in range(2, n+1):
        if a[i] and a[n-i]:
            answer.extend([i, n-i])
            print(' '.join(list(map(str, sorted(answer)))))
            break
    else:
        print(-1)