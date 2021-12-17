import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def gcd(a, b):
    # 최대공약수
    while b != 0:
        temp = a % b
        a, b = b, temp
    return a


n = int(input())
cur = 0
M = None
maxB = 0
for _ in range(n):
    a, b = map(int, input().split())
    cur += a
    if cur < 0:
        temp = b - cur
        maxB = max(maxB, b)
        if not M:
            M = temp
        else:
            M = gcd(M, temp)
            if M <= maxB:
                print(-1)
                break
    else:
        if cur != b:
            print(-1)
            break
    cur = b
else:
    print(M if M else 1)