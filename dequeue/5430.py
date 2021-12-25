import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    cm = input().strip()
    leng = int(input())
    num = deque(eval(input().strip()))
    reverse = 0
    valid = True
    for i in cm:
        if i == "R":
            reverse = 1 - reverse
        else:
            if leng == 0:
                valid = False
                break
            elif reverse == 1:
                num.pop()
                leng -= 1
            elif reverse == 0:
                num.popleft()
                leng -= 1

    if valid:
        if reverse == 1:
            num.reverse()
        print(list(num))
    else:
        print('error')
