import sys
import math
import heapq
sys.stdin = open('input.txt')
input = sys.stdin.readline


def cal_dist(A, B):
    x1, y1 = A
    x2, y2 = B
    dist = math.sqrt(abs(x1-x2)**2 + abs(y1-y2)**2)
    return math.floor(dist)


def main():
    x1, y1, x2, y2 = map(int, input().split())
    a = (x1, y1)
    b = (x2, y2)
    num_list = [a, b]
    isprime = [False, False] + [True] * 10000
    for i in range(len(isprime)):
        if isprime[i]:
            for j in range(2*i, len(isprime), i):
                isprime[j] = False
    n = int(input())
    for _ in range(n):
        x, y = map(int, input().split())
        num_list.append((x, y))
    d = [[] for i in range(len(num_list))]
    distance = [0] + [float('inf')] * (len(d)-1)
    for i in range(len(num_list)):
        for j in range(i, len(num_list)):
            f = num_list[i]
            s = num_list[j]
            dist = cal_dist(f, s)
            if isprime[dist]:
                d[i].append((j, dist))
                d[j].append((i, dist))
    # 다익스트라
    queue = []
    heapq.heappush(queue, (0, 0))
    while queue:
        dis, current = queue.pop()
        if distance[current] < dis:
            continue
        for next_pos, l in d[current]:
            next_dis = l + dis
            if next_dis < distance[next_pos]:
                distance[next_pos] = next_dis
                queue.append((next_dis, next_pos))
    print(distance)
    if distance[1] < 10000:
        print(distance[1])
    else:
        print(-1)
if __name__ == "__main__":
    main()
