sent = "we would also like to share the following document with everyone"
arr = sent.split(" ")
ch = input("Provide Character: ")

# use ch[0] in case user have entered string or word
# it will work for both

for i in range(0,len(arr)):
    if (arr[i][0] == ch[0]):
        print(arr[i])