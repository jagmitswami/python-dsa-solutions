str = "toGGLe cASE"
for i in range(0,len(str)):
    x = ord(str[i])
    if(x>=64 and x<=90):
        print(chr(x+32),end='')
    elif(x>=97 and x<=122):
        print(chr(x - 32), end='')
    else:
        print(str[i],end='')