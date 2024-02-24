# Problem: Reverse a string using a loop.

my_string = "Python"
reversed_string = ""

for char in my_string:
    reversed_string = char + reversed_string

print(reversed_string)