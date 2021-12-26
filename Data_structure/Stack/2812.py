import sys
sys.stdin = open('./input.txt')
input = sys.stdin.readline

n, k = map(int, input().split())
nums = list(map(int, input().strip()))
stack = []

stack.append(int(nums[0]))
for i in nums[1:]:
    num = int(i)
    while True:
        if len(stack) == 0 or k == 0 or num <= stack[-1]:
            stack.append(num)
            break
        elif stack[-1] < num and k > 0:
            stack.pop()
            k -= 1
else:
    for _ in range(k):
        stack.pop()

print("".join(map(str, stack)))
