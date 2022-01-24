import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def up(game_map):
    tp_square = transpose(game_map)
    return transpose(left(tp_square))


def down(game_map):
    tp_square = transpose(game_map)
    return transpose(right(tp_square))


def left(game_map):
    ret = []
    for j in range(n):
        temp = []
        queue = []
        for k in game_map[j]:
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
    return ret


def right(game_map):
    ret = []
    for j in range(n):
        temp = []
        queue = []
        for k in game_map[j][::-1]:
            if k == 0:
                continue
            elif not queue:
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
        ret.append(list(reversed(temp)))
    return ret


def transpose(game_map):
    ret = [j for j in list(zip(*game_map))]
    return ret

T = int(input())
for i in range(1, T+1):
    n, dirt = input().split()
    n = int(n)
    square = [list(map(int, input().split())) for _ in range(n)]
    ret_square = eval(dirt)(square)
    print(f'#{i}')
    for j in range(n):
        print(*ret_square[j])
    del square
    del ret_square
