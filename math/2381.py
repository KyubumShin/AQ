import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
ma = []
pl = []
for _ in range(n):
    x, y = map(int, input().split())
    ma.append(x-y)
    pl.append(x+y)
ma.sort()
pl.sort()
print(max(ma[-1]-ma[0], pl[-1]-pl[0]))
