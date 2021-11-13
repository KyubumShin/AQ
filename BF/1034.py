import sys
from itertools import combinations
sys.stdin = open('input.txt')
input = sys.stdin.readline

dic = {'b': 1, 'd': 2, 'e': 3, 'f': 4, 'g': 5, 'h': 6, 'j': 7, 'k': 8, 'l': 9, 'm': 10,
       'o': 11, 'p': 12, 'q': 13, 'r': 14, 's': 15, 'u': 16, 'v': 17, 'w': 18, 'x': 29,
       'y': 20, 'z': 21}

n, k = map(int, input().split())
word = []
for _ in range(n):
    word.append(set(input().strip()[4:-4]).difference('a', 'n', 't', 'c', 'i'))

print(word)