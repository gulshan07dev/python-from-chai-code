# Problem: Create a function that returns both the area and 
# circumference of a circle given its radius.

import math

def circle_stats(radius):
    area = math.ceil(math.pi * radius ** 2)
    circumference = math.ceil(2 * math.pi * radius)
    return area, circumference

a, c = circle_stats(5)
print("Area: {}, Circumference: {}".format(a, c))