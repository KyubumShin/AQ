import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def main():
    n = int(input())
    k = int(input())
    if k >= n:
        print(0)
    sensor = sorted(list(map(int, input().split())))
    sensor_length = sorted([sensor[i+1] - sensor[i] for i in range(len(sensor)-1)])
    print(sum(sensor_length[:-k+1]))


if __name__ == "__main__":
    main()

