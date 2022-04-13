import sys
import heapq
sys.stdin = open('input.txt')
input = sys.stdin.readline


class dubble_heap:
    def __init__(self):
        self.size = 0
        self.visited = [False] * 1000001
        self.minheap, self.maxheap = [], []

    def input(self, client, priority):
        heapq.heappush(self.minheap, (priority, client))
        heapq.heappush(self.maxheap, (-priority, client))
        self.visited[client] = True
        self.size += 1

    def pop_max(self):
        if self.size == 0:
            return 0
        self.size -= 1
        while self.maxheap:
            _, client = heapq.heappop(self.maxheap)
            if self.visited[client]:
                self.visited[client] = False
                return client
        else:
            return 0

    def pop_min(self):
        if self.size == 0:
            return 0
        self.size -= 1
        while self.minheap:
            _, client = heapq.heappop(self.minheap)
            if self.visited[client]:
                self.visited[client] = False
                return client
        else:
            return 0


dh = dubble_heap()
flag = True
while flag:
    line = list(map(int, input().split()))
    if line[0] == 0:
        flag = False
        continue
    if line[0] == 1:
        _, client, priority = line
        dh.input(client, priority)
    else:
        if line[0] == 2:
            print(dh.pop_max())
        else:
            print(dh.pop_min())