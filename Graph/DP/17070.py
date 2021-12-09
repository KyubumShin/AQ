import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
rooms = []
for _ in range(N):
    room = list(map(int, input().split()))
    rooms.append(room)
dp = [[[0, 0, 0] for _ in range(N)] for _ in range(N)]
dp[0][1][0] = 1
direct = [[1, 0], [0, 1], [1, 1]]
for row in range(N):
    for col in range(N):
        for i in range(3):
            if dp[row][col][i] != 0:
                if col < N-1 and row < N-1 and rooms[row+1][col] == 0 and rooms[row][col+1] == 0 and rooms[row+1][col+1] == 0:
                    dp[row+1][col+1][2] += dp[row][col][i]
                if row < N-1 and rooms[row+1][col] == 0:
                    dp[row+1][col][1] += direct[i][1] * dp[row][col][i]
                if col < N-1 and rooms[row][col+1] == 0:
                    dp[row][col+1][0] += direct[i][0] * dp[row][col][i]
print(sum(dp[-1][-1]))







