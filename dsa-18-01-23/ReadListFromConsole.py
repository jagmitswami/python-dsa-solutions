# write a program to read an array of integers

'''we can use try-catech block idf th user enters wrong type of input'''

# 1st way
print("Enter integers to take as input separated by space: ")
string_of_integers = input()

list = string_of_integers.split(" ")

for i in range(0, len(list)):
    list[i] = int(list[i])

print(list)


# 2nd way
print("-------------------------------------")
print("Enter length of the list: ")

n = int(input())
list = []

for i in range(0, n):
    print("Enter", i + 1, "integer: ")
    list.append(int(input()))

print(list)
