# union_find
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
G = int(input())
P = int(input())
parent = {i: i for i in range(G+1)}


def find(node):
    if parent[node] == node:
        return node
    parent[node] = find(parent[node])
    return parent[node]

answer = 0

for _ in range(P):
    docking = find(int(input()))
    if docking == 0:
        break
    parent[docking] = parent[docking-1]
    answer += 1
print(answer)