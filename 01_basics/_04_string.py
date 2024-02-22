# String Creation
my_string = "Hello, World!"

# String Length
print(len(my_string))  # Output: 13

# Accessing Characters
print(my_string[0])   # Output: 'H'
print(my_string[-1])  # Output: '!'

# Slicing
print(my_string[0:5])  # Output: 'Hello'
print(my_string[7:])   # Output: 'World!'

# String Concatenation
another_string = "How are you?"
concatenated_string = my_string + " " + another_string
print(concatenated_string)  # Output: 'Hello, World! How are you?'

# String Methods
my_string = "hello, world!"

# Capitalize the first letter of the string
print(my_string.capitalize())  # Output: 'Hello, world!'

# Convert the string to uppercase
print(my_string.upper())  # Output: 'HELLO, WORLD!'

# Replace occurrences of a substring
print(my_string.replace("world", "Python"))  # Output: 'hello, Python!'

# Split the string into a list of substrings
print(my_string.split(","))  # Output: ['hello', ' world!']

# Check if the string starts with a certain substring
print(my_string.startswith("hello"))  # Output: True

# Check if the string ends with a certain substring
print(my_string.endswith("world!"))  # Output: True

# String Formatting
name = "Gulshan"
age = 30
print("My name is {} and I am {} years old.".format(name, age))
# Output: 'My name is Alice and I am 30 years old.'

# Using f-strings
print(f"My name is {name} and I am {age} years old.")
# Output: 'My name is Alice and I am 30 years old.'
