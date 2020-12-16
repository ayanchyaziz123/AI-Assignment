from queue import Queue
from collections import defaultdict
import sys


class BFS:
    def __init__(self, graph, source, v):
        visited = {}
        parent = {}
        dis = {}
        level = {}
        output = []
        q = Queue()
        print(v)
        print(graph.keys())
        for x in graph.keys():
            visited[x]=False
            parent[x]=None
            level[x]=None
            dis[x]=-1

        visited[source]=True
        dis[source]=0
        level[source]=0

        q.put(source)

        while not q.empty():
            u=q.get()
            output.append(u)

            for v in graph[u]:
                if not visited[v]:
                    visited[v]=True
                    parent[v]=u
                    dis[v]=dis[u] + 1
                    level[v]=level[u] + 1
                    q.put(v)
        gr=defaultdict(list)
        print(output)
        print("Nodes", " ", "Level")
        for i in range(v):
           p=level[i]
           gr[p].append(i)
           print(" ", i,  " --> ", level[i])
        for i in gr:
           print(i, "--> ", gr[i])




if __name__ == "__main__":
    sys.stdin=open("input.txt", "r")
    graph=defaultdict(list)
    v, e=map(int, input().split())
    for i in range(e):
        n, m=map(int, input().split())
        graph[n].append(m)
        graph[m].append(n)
    source=int(input())
    bbb=BFS(graph, source, v)
