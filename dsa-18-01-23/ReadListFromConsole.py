# write a program to read an array of integers

'''we can use try-catech block idf th user enters wrong type of input'''

# 1st way
print("Enter integers to take as input separated by space: ")
string_of_integers = input()

list1 = string_of_integers.split(" ")

for i in range(0, len(list)):
    list1[i] = int(list1[i])

print(list1)


# 2nd way
print("-------------------------------------")
print("Enter length of the list: ")

n = int(input())
list2 = []

for i in range(0, n):
    print("Enter", i + 1, "integer: ")
    list2.append(int(input()))

print(list2)
