# 에라토네스의 체
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

min_n, max_n = map(int, input().split())
arr = [1] * (max_n - min_n+1)

i = 2
while i**2 <= max_n:
    n = min_n // i**2
    while n*i*i <= max_n:
        if i*i*n-min_n >= 0:
            arr[i*i*n-min_n] = 0
        n += 1
    i += 1
print(sum(arr))