'''enter roll no of 10 students followed by their marks in 3 subject calculate their % marks
and print the roll no along with % of top three students'''

# List of dictionaries of 10 students containing their details
students = [
    {"roll": 1, "marks": 250},
    {"roll": 2, "marks": 230},
    {"roll": 3, "marks": 150},
    {"roll": 4, "marks": 290},
    {"roll": 5, "marks": 280},
    {"roll": 6, "marks": 170},
    {"roll": 7, "marks": 220},
    {"roll": 8, "marks": 270},
    {"roll": 9, "marks": 245},
    {"roll": 10, "marks": 200}
]

# length of the list
n = len(students)

# Calculating percentage of the students and storing it with their other details
for i in range(0, n):
    value = students[i].get("marks")
    percentage = value * 100 / 300

    # rounding off to 1 decimal point only
    percentage = round(percentage, 1)

    # storing percentage
    students[i]["percentage"] = percentage

# sorting
for i in range(0, n):
    for j in range(0, n - i - 1):
        if students[j].get("marks") < students[j + 1].get("marks"):
            temp = students[j]
            students[j] = students[j + 1]
            students[j + 1] = temp

for i in range(0, 3):
    print(students[i])
