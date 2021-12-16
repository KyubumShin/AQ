import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
r_l = list(map(int, input().split()))
city = list(map(int, input().split()))

min_city = city[0]
answer = 0
for i in range(len(city)-1):
    min_city = min(city[i], min_city)
    answer += min_city * r_l[i]
print(answer)