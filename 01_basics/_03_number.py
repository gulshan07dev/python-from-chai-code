import math
from decimal import Decimal
import random

# Basic mathematical operations
a = 10
b = 3

print("Sum:", a + b)
print("Difference:", a - b)
print("Product:", a * b)
print("Quotient:", a / b)  # Normal division
print("Exponent cal:", a ** b)  # Exponent calculate
print("Floor Division:", a // b)  # Floor division (rounded down)
print("Remainder:", a % b)  # Modulo (remainder)

# Other math functions
print("Square Root:", math.sqrt(a))
print("Power:", math.pow(a, 2))
print("Absolute Value:", abs(-5))

# Constants in the math module
print("Pi:", math.pi)
print("Euler's Number:", math.e)


print(repr("chai"))
print(str("chai"))
print("chai")

print(random.random())
print(random.randint(1, 101))

l1 = ["chai", "code", "hello", "ola"]
random.shuffle(l1)
print(l1)
print(random.choices(l1))

mySet = {1, 2, 3}
myEmptySet = set()

print(myEmptySet)
print(mySet)

print(dir(mySet))
mySet.remove(1)
print(mySet)

print(Decimal(2) + Decimal(2.23))