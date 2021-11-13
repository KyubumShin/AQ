import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, r, c = map(int, input().split())


def d_and_c(num, row, col):
    if num == 0:
        return 0
    half_len = 2**(num-1)
    square = half_len**2
    r_weight, row = (1, row-half_len) if row >= half_len else (0, row)
    c_weight, col = (1, col-half_len) if col >= half_len else (0, col)
    print(half_len, r_weight, c_weight, row, col)
    num = 2 * r_weight * square + c_weight * square + d_and_c(num-1, row, col)
    return num


print(d_and_c(N, r, c))
