# Python3 program to print the level  
# with the maximum number of nodes  
  
# Function for DFS in a tree  
def dfs(node, parent, height, vis, tree):  
  
    # calculate the level of every node  
    height[node] = 1 + height[parent]  
  
    # mark every node as visited  
    vis[node] = 1
  
    # iterate in the subtree  
    for it in tree[node]:  
  
        # if the node is not visited  
        if vis[it] == 0:  
  
            # call the dfs function  
            dfs(it, node, height, vis, tree)  
          
# Function to insert edges  
def insertEdges(x, y, tree):  
  
    tree[x].append(y)  
    tree[y].append(x)  
  
# Function to print all levels  
def printLevelswithMaximumNodes(N, vis, height):  
  
    mark = [0] * (N + 1)  
  
    maxLevel = 0
    for i in range (1, N + 1):  
  
        # count number of nodes  
        # in every level  
        if vis[i] == 1:  
            mark[height[i]] += 1
  
        # find the maximum height of tree  
        maxLevel = max(height[i], maxLevel)  
      
    maxi = 0
  
    for i in range(1, maxLevel + 1):  
        maxi = max(mark[i], maxi)  
      
    # print even number of nodes  
    print("The levels with maximum number",  
                "of nodes are:", end = " ")  
    for i in range(1, maxLevel + 1):  
        if mark[i] == maxi:  
            print(i, end = " ")  
  
# Driver Code 
if __name__ == "__main__": 
      
    # Construct the tree  
    N = 9
  
    # Create an empty 2-D list 
    tree = [[] for i in range(N + 1)] 
  
    insertEdges(1, 2, tree)  
    insertEdges(1, 3, tree)  
    insertEdges(2, 4, tree)  
    insertEdges(2, 5, tree)  
    insertEdges(5, 7, tree)  
    insertEdges(5, 8, tree)  
    insertEdges(3, 6, tree)  
    insertEdges(6, 9, tree)  
  
    height = [None] * (N + 1)  
    vis = [0] * (N + 1)  
  
    height[0] = 0
  
    # call the dfs function  
    dfs(1, 0, height, vis, tree)  
  
    # Function to print  
    printLevelswithMaximumNodes(N, vis, height)  
      
# This code is contributed  
# by Rituraj Jain 