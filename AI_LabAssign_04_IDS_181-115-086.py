from collections import defaultdict
import sys
from itertools import repeat

mx = []
arr = []
res = dict(zip(range(10), repeat(None))) 



def dfs(node, parent, height, vis, tree):  
  
    # calculate the level of every node  
    # if node is not equal to parent 
    if node != parent:
        arr.append(node)
        height[node] = 1 + height[parent]  
        print("Explored", node  ,"at depth ", height[node] - 1)
        parent = node
        c = height[node] - 1
        mx.append(c)
  
    # mark every node as visited  
    vis[node] = 1
  
    # iterate in the subtree  
    for it in tree[node]:  
  
        # if the node is not visited  
        if not vis[it]:  
  
            # call the dfs function  
            dfs(it, node, height, vis, tree) 
      
    
if __name__ == "__main__":
    sys.stdin = open("input.txt", "r")
    #define dictionary as a name tree
    tree = defaultdict(list)
    #to get user input vertex and edges
    v, e = map(int, input().split())
    height = [None] * (v + 1)  
    vis = [None] * (v + 1) 
    for i in range(e):
        n1, n2 = map(int, input().split())
        tree[n1].append(n2)
        tree[n2].append(n1)
    source = int(input())
    height[source] = 1
    arr.append(source)
    print("Explored", source  ,"at depth ", height[source] - 1)
    
        #call dfs function
    dfs(source, source, height, vis, tree) 


    for i in range(0, 10):
        print("When depth limit: ", i)
        print()
        for j in range(0, len(arr)):
            if height[arr[j]] - 1 <= i:
                print("Explored ", arr[j], "at depth ", height[arr[j]] - 1)
        print()




    
   


        
     
