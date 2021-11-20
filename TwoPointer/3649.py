import sys, bisect
sys.stdin = open('input.txt')
input = sys.stdin.readline


def solution():
    is_input = input().strip()
    if is_input == '':
        return False
    x = int(is_input)
    n = int(input())
    lengths = []
    for _ in range(n):
        lengths.append(int(input()))
    lengths.sort()
    x = x * 10000000
    right = 0
    left = bisect.bisect_left(lengths, x) - 1
    while right < left:
        join_length = lengths[right] + lengths[left]
        if join_length == x:
            print('yes', lengths[right], lengths[left])
            break
        elif join_length < x:
            right += 1
        else:
            left -= 1
    else:
        print('danger')
    return True


if __name__ == '__main__':
    isRun = True
    while isRun:
        isRun = solution()
