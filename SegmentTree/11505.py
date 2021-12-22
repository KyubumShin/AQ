# segment tree
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
n, m, k = map(int, input().split())
nums = [int(input()) for _ in range(n)]
seg_tree = [0] * n * 4
mod = 1000000007


def init_tree(start, end, node):
    if start == end:
        seg_tree[node] = nums[start]
    else:
        mid = (start + end)//2
        seg_tree[node] = init_tree(start, mid, node*2) * init_tree(mid+1, end, node*2 + 1) % mod
    return seg_tree[node]


def time_tree(start, end, node, left, right):
    if left > end or right < start:
        return 1
    if left <= start and end <= right:
        return seg_tree[node]
    mid = (start + end) // 2
    return time_tree(start, mid, node * 2, left, right) * time_tree(mid + 1, end, node * 2 + 1, left, right) % mod


def update_tree(start, end, node, index, value):
    if index < start or index > end:
        return
    if start == end:
        seg_tree[node] = value
        return

    mid = (start + end) // 2
    update_tree(start, mid, node * 2, index, value)
    update_tree(mid + 1, end, node * 2 + 1, index, value)

    seg_tree[node] = seg_tree[node * 2] * seg_tree[node * 2 + 1] % mod


init_tree(0, n-1, 1)

for _ in range(m+k):
    a, b, c = map(int, input().split())
    if a == 1:
        update_tree(0, n-1, 1, b-1, c)
        nums[b - 1] = c
    elif a == 2:
        print(time_tree(0, n-1, 1, b-1, c-1))
