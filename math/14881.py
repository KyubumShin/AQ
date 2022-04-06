import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline


def gcd(a, b):
    if a > b:
        a, b = b, a
    if b % a == 0:
        return a
    else:
        return gcd(b % a, a)


n = int(input())
for _ in range(n):
    a, b, c = map(int, input().split())
    if c > a and c > b:
        print('NO')
    elif c % gcd(a, b) == 0:
        print("YES")
    else:
        print("NO")
