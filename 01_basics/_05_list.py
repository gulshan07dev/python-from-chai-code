# List Creation
my_list = [1, 2, 3, 4, 5]

# List Length
print(len(my_list))  # Output: 5

# Accessing Elements
print(my_list[0])   # Output: 1
print(my_list[-1])  # Output: 5

# Slicing
print(my_list[1:4])  # Output: [2, 3, 4]
print(my_list[:3])   # Output: [1, 2, 3]
print(my_list[0:-1:2])   # Output: [1, 3, 5]  // step by 1

# List Concatenation
another_list = [6, 7, 8]
concatenated_list = my_list + another_list
print(concatenated_list)  # Output: [1, 2, 3, 4, 5, 6, 7, 8]

# List Methods
my_list = [3, 1, 2, 5, 4]

# Append an element to the end of the list
my_list.append(6)
print(my_list)  # Output: [3, 1, 2, 5, 4, 6]

# Sort the list in ascending order
my_list.sort()
print(my_list)  # Output: [1, 2, 3, 4, 5, 6]

# Reverse the elements of the list
my_list.reverse()
print(my_list)  # Output: [6, 5, 4, 3, 2, 1]

# Remove the first occurrence of a value
my_list.remove(3)
print(my_list)  # Output: [6, 5, 4, 2, 1]

# Insert an element at a specific index
my_list.insert(2, 3)
print(my_list)  # Output: [6, 5, 3, 4, 2, 1]

# Remove and return the last element of the list
popped_element = my_list.pop()
print(popped_element)  # Output: 1
print(my_list)         # Output: [6, 5, 3, 4, 2]

# List Comprehension
squared_numbers = [x**2 for x in my_list]
print(squared_numbers)  # Output: [36, 25, 9, 16, 4]

# Check if an element is in the list
print(3 in my_list)  # Output: True

# Count the occurrences of an element in the list
print(my_list.count(3))  # Output: 1
