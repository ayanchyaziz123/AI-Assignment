from collections import defaultdict
import sys

mx = []


def dfs(node, parent, height, vis, tree, dest):  
  
    # calculate the level of every node  
    # if node is not equal to parent 
    if node != parent:
        height[node] = 1 + height[parent]  
        parent = node
        print("Explored", node  ,"at depth ", height[node] - 1)
        c = height[node] - 1
        mx.append(c)
  
    # mark every node as visited 
    if height[node] - 1 == dest:
        return 
    vis[node] = 1
    
  
    # iterate in the subtree  
    for it in tree[node]:  
  
        # if the node is not visited  
        if not vis[it]:  
  
            # call the dfs function  
            dfs(it, node, height, vis, tree, dest) 
      
    
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
    dest = int(input())
    height[source] = 1
    mx.append(height[source] - 1)
    print("Explored", source  ,"at depth ", height[source] - 1)
    
    #call dfs function

    dfs(source, source, height, vis, tree, dest) 
    m = max(mx)
    print()
    print("Maximum Depth reached: ", m)


        
     
