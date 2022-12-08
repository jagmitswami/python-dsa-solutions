list= [[1,2,3],[4,5,6]]

rows= len(list)
cols= len(list[0])

transpose= [[0]*rows]*cols

for i in range(0,rows):
    for j in range(0,cols):
        transpose[j][i] = list[i][j]
        print(j,i,transpose)
print(transpose)
