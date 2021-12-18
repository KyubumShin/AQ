import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    v, e = map(int, input().split())
    route = [[] for _ in range(v+1)]
    visit = [0] * (v + 1)
    for _ in range(e):
        a, b = map(int, input().split())
        route[a].append(b)
        route[b].append(a)

    queue = []
    valid = True
    group = 1
    print(route)
    for i in range(1, v+1):
        if visit[i] == 0:
            queue.append(i)
            visit[i] = group
            while queue and valid:
                cur_node = queue.pop()
                team = visit[cur_node]
                for node in route[cur_node]:
                    if visit[node] == 0:
                        visit[node] = -1 * team
                        queue.append(node)
                    else:
                        if visit[cur_node] == visit[node]:
                            valid = False
                            print(valid)
                print(visit)
    if valid:
        print("YES")
    else:
        print("NO")