import sys
sys.stdin = open('./input.txt')
input = sys.stdin.readline
n, m = map(int, input().split())
nums = []
for _ in range(n):
    nums.append(int(input()))
seg_tree = [0] * n * 4


def init_tree(start, end, node):
    if start == end:
        seg_tree[node] = nums[start]
        return seg_tree[node]
    mid = (start + end)//2
    seg_tree[node] = min(init_tree(start, mid, node*2), init_tree(mid +1, end, node*2 + 1))
    return seg_tree[node]


def min_tree(start, end, node, left, right):
    if left > end or right < start:
        return float('inf')
    if left <= start and end <= right:
        return seg_tree[node]
    mid = (start + end)//2
    return min(min_tree(start, mid, node * 2, left, right), min_tree(mid+1, end, node * 2+1, left, right))


init_tree(0, n-1, 1)
print(seg_tree)
for _ in range(m):
    a, b = map(int, input().split())
    print(min_tree(0, n-1, 1, a-1, b-1))