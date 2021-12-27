import sys
import re
sys.stdin = open('input.txt')
input = sys.stdin.readline


def getpi(p):
    m = len(p)
    pi = [0] * m
    i = 1
    leng = 0
    while i < len(p):
        if p[i] == p[leng]:
            leng += 1
            pi[i] = leng
            i += 1
        else:
            if leng != 0:
                leng = pi[leng-1]
            else:
                pi[i] = 0
                i += 1
    return pi


def kmp(p, s) -> bool:
    answer = []
    pi = getpi(p)
    n = len(s)
    m = len(p)
    j = 0
    for i in range(n):
        while j>0 and s[i] != p[j]:
            j = pi[j-1]
        if s[i] == p[j]:
            if j == m-1:
                answer.append(i-m+1)
                j = pi[j]
            else:
                j += 1
    return answer


def main():
    t = input()
    p = input()
    new_t = re.sub('[0-9]', '', t)
    print(new_t)
    ans = kmp(p, new_t)
    ans = list(map(lambda x: x+1, ans))
    print(len(ans))


if __name__ == "__main__":
    main()