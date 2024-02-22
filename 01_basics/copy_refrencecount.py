# Understanding Copy and Reference Count: Internal Working

# We can assign the same object reference to multiple variables.
# Is there any method in Python to get the reference count of an object?

# Yes, we can use the sys.getrefcount() method from the sys module.
import sys
print(sys.getrefcount(123))
# The sys.getrefcount() function returns the reference count
# of an object. However, for small integers and strings,
# due to interpreter optimization, the reference count may not
# accurately reflect the actual number of references to the object.
# This optimization is performed because small integers and 
# strings are frequently used and Python optimizes the reference
# counting mechanism for them.
 
print(sys.getrefcount(123))  # 4294967295
print(sys.getrefcount("Gulshan"))  # 4294967295
print(sys.getrefcount([1, 2, 3]))  # 1
print(sys.getrefcount(1234567))  # 3

# Let's understand this code:
a = 5 
# NOTE: in python data type is not assign to variable it assign to object
a = "chai" 
# you might thinking created a new refrence and assign to a 
# variable and previous object garbage collected,
# you are right but here is exception with number and string.

# NOTE: Objects like numbers and strings are not immediately 
# garbage collected because they are used frequently.
# Python delays garbage collection for these objects
# in case they might be used again soon. This optimization
# improves performance by avoiding unnecessary garbage collection 
# of frequently used objects.


# Let's understand this code:
a = 5
b = 2
a = a + 2
# This will create a new object '7' and assign it to variable 'a'.
# The previous object '5' might be garbage collected later.

# Now, let's see an example with lists:
myListOne = [1, 2, 3]
myListTwo = myListOne
# Assign the same object memory reference to both variables.

myListOne[0] = 33
print(myListTwo)  # Output: [33, 2, 3]
# Since lists are mutable, changing 'myListOne' also affects 'myListTwo'
# because they both reference the same object.

# Different ways of creating a copy:
x = [1, 2, 3]
y = x.copy()  # Using the copy() method
y = x[:]  # Using slicing
  