'''create an empty array and write a function to calculate
factorial of individual elements of the array  and store it in the new array
'''

num_arr = [1, 3, 5, 7, 9, 15]
factorial_arr = []


# Function to calculate factorial of the passed element
def calFactorial(e):
    res = 1
    for j in range(1, e + 1):
        res *= j

    return res


for i in range(0, len(num_arr)):
    fact = calFactorial(num_arr[i])
    factorial_arr.append(fact)

print(factorial_arr)
