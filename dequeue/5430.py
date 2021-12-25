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
        elif i == "D":
            if not num:
                valid = False
                break
            else:
                if reverse == 1:
                    num.pop()
                elif reverse == 0:
                    num.popleft()

    if valid:
        if reverse == 1:
            num.reverse()
        print("[" + ",".join(list(map(str, num))) + "]")
    else:
        print('error')
