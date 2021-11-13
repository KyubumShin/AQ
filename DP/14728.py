#배낭문제
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, T = map(int, input())
subject = []
for _ in range(N):
    time, score = map(int, input())
    subject.append(time, score)

