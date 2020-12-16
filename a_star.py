import sys

def make2dList(rows, cols):
    a=[]
    for row in range(rows): a += [[0]*cols]
    return a

if __name__ == "__main__":
    sys.stdin = open("input.txt", "r")
    r = 3
    arr = []
    a = []
    matrix = []
    rows = 3
    cols = 6
    a = make2dList(rows, cols)
    for i in range(0, r):
        st = str(input())
        arr.append(st)     
    for i in range(0 , r):
        matrix.append(arr[i])
    for i in range(0, rows):
        for j in range(0, cols):
            if matrix[i][j] == '#':
                a[i][j] = 1       
    for i in range(0, 3):
        for j in range(0, 6):
            print(a[i][j], end=' ')
        print()                 
            

    
            
                        
                 
             