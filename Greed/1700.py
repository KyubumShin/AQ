import sys
from collections import Counter
sys.stdin = open('input.txt')
input = sys.stdin.readline

n, k = map(int, input().split())
plug = [0] * n
lst = list(map(int, input().split()))
answer = 0
if n >= k:
    print(0)
else:
    for i, x in enumerate(lst):
        max_index, swap = 0, 0
        if x in plug:
            pass
        elif 0 in plug:
            plug[plug.index(0)] = x
        else:
            for j in plug:
                if j not in lst[i:]:
                    swap = j
                    break
                elif max_index != max(lst[i:].index(j), max_index):
                    swap = j
            plug[plug.index(swap)] = i
            answer += 1
print(answer)