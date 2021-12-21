import sys
import time
sys.stdin = open('input.txt')
input = sys.stdin.readline

def main():
    n, m = map(int, input().split())
    n_list = list(map(int, input().split()))
    mod_list = [0] * m
    total = 0
    answer = 0
    for i in n_list:
        total = (total+i) % m
        if total == 0:
            answer += 1
        mod_list[total] += 1

    for i in mod_list:
        answer += i * (i-1) // 2
    print(answer)


if __name__ == "__main__":
    main()
