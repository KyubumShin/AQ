import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

T = int(input())

def find(x):
    low, high = 1, 141
    mid = (low + high)//2
    while (mid-1)*mid//2 >= x or x > mid*(mid+1)//2:
        if x > mid*(mid+1)//2:
            low = mid + 1
        else:
            high = mid
        mid = (low + high)//2
    return (mid, x - mid*(mid-1)//2)

for test_case in range(1, T+1):
    a, b = map(int, input().split())
    if a > b:
        a, b = b, a
    row_a, col_a = find(a)
    row_b, col_b = find(b)
    print(a, row_a, col_a)
    print(b, row_b, col_b)
    ans = col_a - col_b + row_b - row_a if col_a > col_b else max(row_b-row_a, col_b-col_a)
    print('#{} {}'.format(test_case, ans))