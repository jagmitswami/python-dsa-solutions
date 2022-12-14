list= [[12,2,37],[422,57,61]]

rows= len(list)
cols= len(list[0])

maximum = -1000000000
position_row = -1
position_col  = -1
for i in range(0,rows):
    for j in range(0,cols):
        if(list[i][j]>maximum):
            maximum =  list[i][j]
            position_row = i
            position_col = j
print(maximum,position_row,position_col)