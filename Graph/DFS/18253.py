import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline

def main():
    n, a, b = map(int, input().split())
    MIN = 1
    MAX = n
    Ore = deque()
    Sixre = deque()
    Ore.append([a])
    Sixre.append([b])
    day = 0
    while Ore and Sixre:
        dis = 1 << day
        ore_point = Ore.popleft()
        sixre_point = Sixre.popleft()
        next_Ore_point = []
        next_sixre_point = []
        while ore_point:
            point = ore_point.pop()
            if point + dis <= MAX:
                next_Ore_point.append(point + dis)
            if point - dis >= MIN:
                next_Ore_point.append(point - dis)
        if len(next_Ore_point) > 0:
            Ore.append(next_Ore_point)
        while sixre_point:
            point = sixre_point.pop()
            if point + dis <= MAX:
                next_sixre_point.append(point + dis)
                if point + dis in next_Ore_point:
                    return day + 1
            if point - dis >= MIN:
                next_sixre_point.append(point - dis)
                if point - dis in next_Ore_point:
                    return day + 1
        if len(next_sixre_point) > 0:
            Sixre.append(next_sixre_point)
        day += 1
    else:
        return -1

if __name__ == "__main__":
    answer = main()
    print(answer)



