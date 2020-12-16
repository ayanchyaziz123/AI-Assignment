from collections import defaultdict
import sys
import queue

def bfs(graph, source, V):
    level = [None] * (V+1)
    parent = [None] * (V + 1)
    visited = [False] * (V + 1)

    level[source] = 1
    visited[source] = True
    que = queue.Queue()
    que.put(source)

    while not que.empty():
        prev = que.get()
        print(prev)

        for neighbour in graph[prev]:
            if neighbour not in visited[i]:
                level[neighbour] = level[prev] + 1
                parent[neighbour] = prev
                visited[neighbour] = True
                que.put(neighbour) 

if __name__ == "__main__":
    sys.stdin = open("input.txt", "r")
    V, E = map(int, input().split())
    graph = defaultdict(list)
    for i in range(E):
        node1, node2 = map(str, input().split())
        graph[node1].append(node2)
        graph[node2].append(node1)
        bfs(graph, 0, V)
       


