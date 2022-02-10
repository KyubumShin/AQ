import sys
from itertools import combinations
sys.stdin = open('input.txt')
input = sys.stdin.readline

n, m = map(int, input().split())
people = []

for i in range(m):
    temp = list(map(int, input().split()))
    a = 0
    if temp[0] == n:
        print(1)
        sys.exit()
    for j in temp[1:]:
        a |= 1 << (j-1)
    people.append(a)

for k in range(2, m+1):
    combs = list(combinations(people, k))
    for nums in combs:
        temp = 0
        for num in nums:
            temp |= num
            if temp == (1<<n)-1:
                print(k)
                sys.exit()
else:
    print(-1)
