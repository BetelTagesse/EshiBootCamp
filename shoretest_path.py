# imports
from collections import defaultdict, deque
from curses import pair_content
import sys
import heapq
import csv
#from tracemalloc import start


class Node:

    def __init__(self, name):
        self.name = name
        self.edge_list = []

    def connect(self, node):
        con = (self, node)
        self.edge_list.append(con)


class Edge:

    def __init__(self, left, right, weight=1):
        self.left = left
        self.right = right
        self.weight = weight


class Graph:

    def __init__(self):
        self.verticies = {}
        self.edges = {}
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
        e = Edge(left, right, weight=1)

        key = (left.name, right.name)
        self.edges[key] = e

        key = (right.name, left.name)
        self.edges[key] = e

        left.connect(right)
        right.connect(left)

    def BFS(self, start, dest):
        visited = set()

        q = deque([(start.name, [start.name], 0)])
        visited.add(start.name)

        while q:
            n, p, t = q.popleft()
            if n == dest.name:
                return p

            for neighbour in self.neighbours[n]:
                if neighbour not in visited:
                    q.append((neighbour[0], p+[neighbour[0]], t+neighbour[1]))
                    visited.add(neighbour)

        return []

    def DFS(self, start, dest):
        visited = set()

        stack = [(start.name, [start.name], 0)]
        visited.add(start.name)
        while stack:
            n, p, t = stack.pop()
            if n == dest.name:
                return p

            for neighbour in self.neighbours[n]:
                if neighbour not in visited:
                    stack.append(
                        (neighbour[0], p+[neighbour[0]], t+neighbour[1]))
                    visited.add(neighbour)

        return []

    def Dijkstra(self, start, dest):
        minHeap = [(0, start.name, [start.name])]
        visited = set()

        while minHeap:
            w, n, p = heapq.heappop(minHeap)
            if n == dest.name:
                return p
            if n in visited:
                continue
            visited.add(n)

            for new_node, new_weight in self.neighbours[n]:
                if new_node not in visited:
                    heapq.heappush(
                        minHeap, (w + new_weight, new_node, p + [new_node]))

        return []


g = Graph()

with open('./data.csv', newline = '') as file:

    data = csv.reader(file, delimiter=',')

    for row in data:
        start = Node(row[0])
        dest = Node(row[1])
        g.add_edge(start, dest, int(row[2]))

Arad = Node('Arad')
Bucharest = Node('Bucharest')
print(g.BFS(Arad, Bucharest))
print(g.DFS(Arad, Bucharest))
print(g.Dijkstra(Arad, Bucharest))
