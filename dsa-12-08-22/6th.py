list= [[0,0,0],[4,5,6],[0,0,1],[0,0,0]]

rows= len(list)
cols= len(list[0])

count_0 = 0
for i in range(0,rows):
    for j in range(0,cols):
        if(list[i][j] == 0):
            count_0 += 1

if(count_0>rows*cols//2):
    print("Sparse Metrics")
else:
    print("Not Sparse Metrics")