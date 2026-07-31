li = ['Hello', 7, (11, 22, 33, 44), {'abhishek': 1, 'anil': 2}, 3.14]

# Find the tuple and dictionary
tuple_index = 2
dictionary = li[3]
print(li[3])

# Swap
tuple_value = li[2]

li[3][li[2]] = li[3].pop("abhishek")
li[2] = "abhishek"

print(li)