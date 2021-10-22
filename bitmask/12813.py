import sys
sys.stdin = open('./input.txt')
input = sys.stdin.readline
length = 100000

A = int(input(), 2)
B = int(input(), 2)
mask = 2**length - 1

print(bin(A & B)[2:].zfill(length))
print(bin(A | B)[2:].zfill(length))
print(bin(A ^ B)[2:].zfill(length))
print(bin(A ^ mask)[2:].zfill(length))
print(bin(B ^ mask)[2:].zfill(length))