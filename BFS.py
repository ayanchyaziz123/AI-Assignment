import sys
from queue import Queue
from collections import defaultdict
sys.stdin = open("input.txt", "r")



class BFS:
    def __init__(self, graph, source):
        visited = {}
        parent = {}
        dis = {}
        level = {}
        q = Queue()
        output = []

        for x in graph.keys():
            visited[x] = False
            parent[x] = None
            level[x] = None
            dis[x] = -1

        visited[source] = True
        dis[source] = 0

        q.put(source)

        while not q.empty():
            u = q.get()
            output.append(u)

            for v in graph[u]:
                if not visited[v]:
                    visited[v] = True
                    parent[v] = u
                    dis[v] = dis[u] + 1
                    q.put(v)

        print(output)


if __name__ == "__main__":
    graph = defaultdict(list)
    N, E = map(int, input().split())
    for i in range(E):
        U, V = map(str, input().split())
        graph[U].append(V)
        graph[V].append(U)
    source = str(input())
    bbb = BFS(graph, source)
