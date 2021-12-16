import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
print(bin(n-1).count('1')%2)