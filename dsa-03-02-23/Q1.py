'''
Write a program to accept a string.
Convert the string to uppercase. Count and output the number of double letter sequences that exist in the string.
Sample Input: “SHE WAS FEEDING THE LITTLE RABBIT WITH AN APPLE” Sample Output: 4'''

print("Enter a string: ")
st = input()
st = st.upper()

count = 0
i = 0
while i < len(st) - 1:
    if st[i] == st[i + 1]:
        count += 1
        i += 1
    i += 1
print(count)
