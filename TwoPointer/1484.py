import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

G = int(input())

right, left = 1, 1
answer = []
while left*left - (left-1)*(left-1) <= G:
    temp_G = (left + right) * (left-right)
    if G == temp_G:
        answer.append(left)
    if temp_G < G:
        left += 1
        continue
    right += 1

if answer:
    for i in answer:
        print(i)
else:
    print(-1)