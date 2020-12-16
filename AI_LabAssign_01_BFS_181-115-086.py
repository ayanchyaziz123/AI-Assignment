import queue
from collections import defaultdict
import sys

def pri(graph, V, x):
    
    ss = x
    level = [None] * V
    marked = [False] * V
    dis = [-1] * V
    parent = [-1] * V

    que = queue.Queue()
    que.put(x)
    level[x] = 1
    marked[x] = True
    dis[x] = 0


    while (not que.empty()):

        x = que.get()
        for i in range(len(graph[x])):
            b = graph[x][i]
            if (not marked[b]):
                que.put(b)
                level[b] = level[x] + 1
                dis[b] = dis[x] + 1
                marked[b] = True
                parent[b] = x
 
    for i in range(V):
        if i == ss:
            continue
        elif dis[i] == -1:
            print(i, "is not reachable")
        else:
            path = []
            s = ss
            n = i
            while(n!=s):
                path.append(n)
                n = parent[n]
            l = len(path)
            print("Minimum",  l  ,"edges needed to reach", i)
            print("Path taken:   ", end=' ')
            print(s, end=' ')
            for i in reversed(path):
                print(i, end=' ')
            print()    
    gr = defaultdict(list)
    print()
    print("Bonus :")
    print()
    for i in range(V):
        p = level[i]
        if not p:
            continue
        gr[p - 1].append(i)
    for i in sorted(gr):
        print("Level ", i, " : ", gr[i])



if __name__ == '__main__':

    #sys.stdin = open("input.txt", "r")
    graph = defaultdict(list)
    v, e = map(int, input().split())
    for i in range(e):
        m, n = map(int, input().split())
        graph[m].append(n)
        graph[n].append(m)
    source = int(input()) 

    pri(graph, v, source)
