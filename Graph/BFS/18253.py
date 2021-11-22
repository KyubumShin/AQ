import sys
import math
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline

def main():
    n, a, b = map(int, input().split())
    MAX = n
    MIN = 1
    arr = [[0] * (n+1) for i in range(math.ceil(math.log2(n+1)))]
    ore = deque()
    sixre = deque()
    ore.append((a, 0))
    sixre.append((b, 0))
    if abs(a-b) % 2 == 1:
        return -1
    while ore:
        point, day = ore.pop()
        dis = 1 << day
        day = day + 1
        if point + dis <= MAX:
            ore.append((point+dis, day))
            arr[day-1][point+dis] = 1
        if point - dis >= MIN:
            ore.append((point-dis, day+1))
            arr[day-1][point-dis] = 1
    while sixre:
        point, day = sixre.pop()
        dis = 1 << day
        if point + dis <= MAX:
            sixre.append((point+dis, day+1))
            if arr[day][point+dis] == 1:
                return day+1
        if point - dis >= MIN:
            sixre.append((point-dis, day+1))
            if arr[day][point-dis] == 1:
                return day+1
    return -1

if __name__ == "__main__":
    answer = main()
    print(answer)



