import sys
sys.stdin = open('./input.txt')
input = sys.stdin.readline

for test_case in range(10):
    n = int(input())
    strings = input().strip()
    stack = []
    token = []
    for s in strings:
        if s.isdigit():
            stack.append(int(s))
        else:
            if s == '(':
                token.append(s)
            elif s == '*':
                token.append(s)
            elif s == '+':
                if not stack:
                    token.append(s)
                else:
                    while token[-1] != '(' and stack:
                        stack.append(token.pop())
                    token.append(s)
            else:
                while token[-1] != '(':
                    stack.append(token.pop())
                token.pop()
    result = []
    for i in stack:
        if isinstance(i, int):
            result.append(i)
        else:
            f = result.pop()
            s = result.pop()
            result.append(f*s if i == '*' else f+s)
    print(f'#{test_case+1} {result[-1]}')