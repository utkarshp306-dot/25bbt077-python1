import random

# Create odd list
odd_list = [random.randrange(1, 50, 2) for i in range(5)]

# Create even list
even_list = [random.randrange(2, 50, 2) for i in range(4)]

print("Odd List:", odd_list)
print("Even List:", even_list)

# Replace third element
odd_list[2] = even_list

print("After Replacing 3rd Element:", odd_list)

# Flatten
flat_list = []
for i in odd_list:
    if isinstance(i, list):
        flat_list.extend(i)
    else:
        flat_list.append(i)

# Sort
flat_list.sort()

print("Flattened & Sorted List:", flat_list)
12:41 p
