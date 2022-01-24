import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def left():
    ret = []
    for j in range(n):
        temp = []
        queue = []
        for k in square[j]:
            if k == 0:
                continue
            if not queue:
                queue.append(k)
            elif queue[-1] == k:
                queue[-1] += k
                temp.extend(queue)
                queue = []
            else:
                queue.append(k)
        else:
            temp.extend(queue)
            while len(temp) < n:
                temp.append(0)
        ret.append(temp)
    del temp
    del queue
    return ret


def rotate():
    return [j for j in list(zip(*square[::-1]))]


T = int(input())
dic = {'left': 0, 'down': 1, 'right': 2, 'up': 3}
for i in range(1, T+1):
    n, dirt = input().split()
    n = int(n)
    square = [list(map(int, input().split())) for _ in range(n)]
    for _ in range(dic[dirt]):
        square = rotate()
    square = left()
    for _ in range((4-dic[dirt]) % 4):
        square = rotate()

    print(f'#{i}')
    for j in range(n):
        print(*square[j])
    del square
