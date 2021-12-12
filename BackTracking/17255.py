import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = str(input().strip())


def check(N):
    if len(N) == 1:
        return 1
    left = N[:-1]
    right = N[1:]
    if left != right:
        return check(left) + check(right)
    else:
        return check(left)

print(check(N))