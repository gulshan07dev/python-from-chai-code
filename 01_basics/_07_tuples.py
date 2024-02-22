# Creating a tuple
my_tuple = (1, 2, 3, 4, 5)
print("Tuple:", my_tuple)

# Accessing elements of a tuple
print("First element:", my_tuple[0])
print("Last element:", my_tuple[-1])

# Tuple slicing
print("Sliced tuple:", my_tuple[1:4])

# Tuple length
print("Length of tuple:", len(my_tuple))
 
# Nested tuples
nested_tuple = ((1, 2), (3, 4), (5, 6))
print("Nested tuple:", nested_tuple)

# Tuple unpacking
a, b, c = my_tuple[:3]
print("Unpacked values:", a, b, c)

# Checking if an element exists in a tuple
print("Is 3 in the tuple?", 3 in my_tuple)
print("Is 9 in the tuple?", 9 in my_tuple)
  
# Tuple is immutable and list is mutable
# my_tuple[0] = 10  # Attempting to modify a tuple will raise an error
 
# Tuple methods
print("Index of 3:", my_tuple.index(3))
print("Count of 2:", my_tuple.count(2))

# Tuple conversion
list_from_tuple = list(my_tuple)
print("Converted to list:", list_from_tuple)

# Deleting a tuple
del list_from_tuple 
print(list_from_tuple)  # Attempting to access a deleted tuple will raise an error
 