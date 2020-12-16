from collections import defaultdict
import sys

if __name__ == "__main__":
    rows = 3
    cols = 6
    matrix2 = [['a']*cols]*rows
    matrix2[2][1] = 'b'
    matrix = [[0]*cols]*rows
    matrix[0][3] = 7
    for i in range(0, 3):
        for j in range(0, 6):
            pass
            #if matrix2[i][j] == 'a':
               # matrix[i][j] = 1 
    for i in range(0, 3):
        for j in range(0, 6):
            print(matrix[i][j], end=' ')
        print()         

