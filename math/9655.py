import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
n = int(input())
print('SK' if n % 2 == 1 else 'CY')