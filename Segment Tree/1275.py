import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
n, m = map(int, input().split())
nums = [i for i in list(map(int, input().split()))]
seg_tree = [0] * n * 4


def init_tree(start, end, node):
    if start == end:
        seg_tree[node] = nums[start]
        return seg_tree[node]
    mid = (start + end)//2
    seg_tree[node] = init_tree(start, mid, node*2) + init_tree(mid +1, end, node*2 + 1)
    return seg_tree[node]


def sum_tree(start, end, node, left, right):
    if left > end or right < start:
        return 0
    if left <= start and end <= right:
        return seg_tree[node]
    mid = (start + end)//2
    return sum_tree(start, mid, node * 2, left, right) + sum_tree(mid+1, end, node * 2+1, left, right)


def update_tree(start, end, node, index, dif):
    if index < start or index > end:
        return
    seg_tree[node] += dif
    if start != end:
        mid = (start + end) // 2
        update_tree(start, mid, node * 2, index, dif)
        update_tree(mid + 1, end, node * 2 + 1, index, dif)


init_tree(0, n-1, 1)
for _ in range(m):
    a, b, c, d = map(int, input().split())
    if a < b:
        print(sum_tree(0, n - 1, 1, a - 1, b - 1))
    else :
        print(sum_tree(0, n - 1, 1, b - 1, a - 1))
    dif = d - nums[c-1]
    nums[c-1] = d
    update_tree(0, n-1, 1, c-1, dif)

