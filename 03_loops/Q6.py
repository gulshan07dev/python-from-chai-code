# Problem: Compute the factorial of a number using a while loop.

number = 5
factorial = 1

while number > 0:
    factorial *= number
    number -= 1

print("Factorial is {}".format(factorial))
