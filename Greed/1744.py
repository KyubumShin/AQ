import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def solution():
    N = int(input())
    positive = []
    negative = []
    answer = 0

    for _ in range(N):
        num = int(input())
        if num == 1:
            answer += 1
        elif num > 0:
            positive.append(num)
        else:
            negative.append(num)

    positive.sort(reverse=True)
    negative.sort()

    if len(positive)%2 == 0:
        for i in range(0, len(positive), 2):
            answer += positive[i] * positive[i+1]
    else:
        for i in range(0, len(positive)-1, 2):
            answer += positive[i] * positive[i+1]
        answer += positive[-1]

    if len(negative)%2 == 0:
        for i in range(0, len(negative), 2):
            answer += negative[i] * negative[i + 1]
    else:
        for i in range(0, len(negative)-1, 2):
            answer += negative[i] * negative[i + 1]
        answer += negative[-1]
    return answer

if __name__ == '__main__':
    print(solution())
