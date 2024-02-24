# Problem: Given a string, find the first non-repeated character.

my_string = "Python"

for char in my_string:
    if my_string.count(char) == 1:
        print("The first non-repeated char is {}".format(char))
        break