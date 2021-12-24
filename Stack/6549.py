import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

def main():
    while True:
        num_list = list(map(int, input().split()))
        if num_list == [0]:
            break
        n = num_list[0]
        graph = num_list[1:]
        stack = [(0, graph[0])]
        graph.append(0)
        result = 0
        for i in range(1, n + 1):
            cursor = i
            while stack and stack[-1][1] > graph[i]:
                cursor, temp = stack.pop()
                result = max(result, temp * (i - cursor))
            stack.append((cursor, graph[i]))
        print(result)

if __name__ == "__main__":
    main()