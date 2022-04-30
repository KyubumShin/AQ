import sys, copy
sys.stdin = open('../input.txt')
input = sys.stdin.readline

points = list(map(int, input().split()))

a, b, c, d = [points[i:i+2] for i in range(0, len(points), 2)]


def ccw(p1, p2, p3):
    cross_product = (p2[0] - p1[0])*(p3[1] - p1[1]) - (p3[0] - p1[0])*(p2[1] - p1[1])

    if cross_product > 0:
        return 1
    elif cross_product < 0:
        return -1
    else:
        return 0


def line_intersection(l1, l2):
    l1_l2 = ccw(l1[0], l1[1], l2[0]) * ccw(l1[0], l1[1], l2[1])
    l2_l1 = ccw(l2[0], l2[1], l1[0]) * ccw(l2[0], l2[1], l1[1])
    return l1_l2 < 0 and l2_l1 < 0


print(1 if line_intersection([a, b], [c, d]) else 0)
