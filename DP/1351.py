import sys
from collections import defaultdict
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, P, Q = map(int, input().split())
A = defaultdict(int)
A[0] = 1


def cal_n(number):
    if A[number] != 0:
        return A[number]
    A[number] = cal_n(number//P) + cal_n(number//Q)
    return A[number]


print(cal_n(N))
