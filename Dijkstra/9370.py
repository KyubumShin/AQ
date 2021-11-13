import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
n, m, t = map(int, input().split())
s, g, h = map(int, input().split())
for _ in range(m):
