def make2dList(rows, cols):
    a=[]
    for row in range(rows): a += [[0]*cols]
    return a

rows = 3
cols = 2
a = make2dList(rows, cols)
a[0][1] = 1
print(a)