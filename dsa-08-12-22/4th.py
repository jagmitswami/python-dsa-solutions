list= [[12,2,37],[422,57,61],[11,22,33],[21,22,23]]
l = len(list)

# to store value declared temp
temp = list[0]
list[0] = list[l-1]
list[l-1] = temp
print(list)