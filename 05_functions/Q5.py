# Problem: Write a function that greets a user. If no name is 
# provided, it should greet with a default name.

def greet(name = "default"):
    return "hello {} !".format(name)

print(greet("Gulshan"))
print(greet())