import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, B = map(int, input().split())
arr = []
for _ in range(N):
    nums = list(map(int, input().split()))
    arr.append(nums)

bin_B = bin(B)[2:]
dp = []
dp.append(arr)


def matrix_mul(a, b):
    result = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                result[i][j] += a[i][k] * b[k][j]
    for i in range(N):
        for j in range(N):
            result[i][j] %= 1000

    return result

for i in range(1, len(bin_B)):
    temp = dp[-1]
    dp.append(matrix_mul(temp, temp))

print(dp)
print(bin_B)
answer = [[1 if i == j else 0 for i in range(N)] for j in range(N)]
for i in range(len(bin_B)):
    if bin_B[-i-1] == '1':
        mat = dp[i]
        answer = matrix_mul(answer, mat)

for row in answer:
    print(*row)
