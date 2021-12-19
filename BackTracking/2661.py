import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
cur = 0
seqs = []

def bt(num):
    for i in range(1, (num//2)+1):
        if seqs[-i:] == seqs[-i*2:-i]:
            return -1

    if num == n:
        print(''.join(list(map(str, seqs))))
        return 0

    for i in range(1, 4):
        seqs.append(i)
        if bt(num + 1) == 0:
            return 0
        seqs.pop()

if __name__ == "__main__":
    bt(0)


