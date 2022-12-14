str = "Diego Armando Maradona"
arr = str.split(" ")
for i in range(0,len(arr)):
    if(i == len(arr)-1):
        print(arr[i])
    else:
        print(arr[i][0]+".",end='')