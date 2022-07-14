
from collections import defaultdict, deque
import sys
import heapq


class Node:

    def __init__(self, name):
        self.name = name
        self.edge_list = []

    def connect(self, node):
        con = (self.name, node.name)
        self.edge_list.append(con)


# class Edge:

#     def init(self, left, right, weight=1):
#         self.left = left
#         self.right = right
#         self.weight = weight


class Graph:

    def __init__(self):
        self.verticies = {}
        self.neighbours = defaultdict(list)

    def add_node(self, node):
        self.verticies[node.name] = node

    def add_edge(self, left, right, weight=1):
        if left.name not in self.verticies:
            self.verticies[left.name] = left

        if right.name not in self.verticies:
            self.verticies[right.name] = right

        self.neighbours[left.name].append((right.name, weight))
        self.neighbours[right.name].append((left.name, weight))
        left.connect(right)
        right.connect(left)

    def BFS(self, start, dest):
        visited = set()

        q = deque([(start, [start], 0)])
        visited.add(start)

        while q:
            n, p, t = q.popleft()
            if n == dest:
                return p

            for neighbour in self.neighbours[n]:
                if neighbour not in visited:
                    q.append((neighbour[0], p+[neighbour[0]], t+neighbour[1]))
                    visited.add(neighbour)

        return []

    # def DFS(self, start, dest):
    #     visited = set()

    #     stack = [(start, [start], 0)]
    #     visited.add(start)
    #     while stack:
    #         n, p, t = stack.pop()
    #         if n == dest:
    #             return p

    #         for neighbour in self.neighbours[n]:
    #             if neighbour not in visited:
    #                 stack.append(
    #                     (neighbour[0], p+[neighbour[0]], t+neighbour[1]))
    #                 visited.add(neighbour)

    #     return []

    # def Dijkstra(self, start, dest):
    #     minHeap = [(0, start, [start])]
    #     visited = set()

    #     while minHeap:
    #         w, n, p = heapq.heappop(minHeap)
    #         if n == dest:
    #             return p
    #         if n in visited:
    #             continue
    #         visited.add(n)

    #         for new_node, new_weight in self.neighbours[n]:
    #             if new_node not in visited:
    #                 heapq.heappush(
    #                     minHeap, (w + new_weight, new_node, p + [new_node]))

    #     return []


a = Node('0')
b = Node('1')
c = Node('2')
d = Node('3')
# e = Node('4')

g = Graph()
g.add_edge(a, b, 2)
g.add_edge(a, c, 2)
g.add_edge(b, c, 1)
g.add_edge(b, d, 1)
g.add_edge(c, d, 2)
print(g.BFS('0', '3'))
# print(g.DFS('0', '3'))
# print(g.Dijkstra('0', '3'))