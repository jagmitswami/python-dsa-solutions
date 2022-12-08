list= [[1,2,3],[4,5,6]]

rows= len(list)
cols= len(list[0])

# creating 2d metrics for transpose
transpose= []
for i in range(0,cols):
    temp = []
    for j in range(0,rows):
        temp.append(0)
    transpose.append(temp)


for i in range(0,rows):
    for j in range(0,cols):
        transpose[j][i] = list[i][j]
print(transpose)