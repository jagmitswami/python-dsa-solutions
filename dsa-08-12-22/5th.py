list= [[1,2,3],[4,5,6]]

rows= len(list)
cols= len(list[0])

# column sum
for i in range(0,rows):
    sum_cols = 0
    for j in range(0,cols):
        sum_cols+= list[i][j]
    list[i].append(sum_cols)

#updateing values
rows= len(list)
cols= len(list[0])

# row sum
temp = []
for i in range(0,cols):
    sum_rows = 0
    for j in range(0,rows):
        sum_rows+= list[j][i]
    temp.append(sum_rows)
list.append(temp)

print(list)