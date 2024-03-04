# Using try finally block for error handling

file = open("test.txt", "w")  # Open file in write mode

try:
    file.write("hello")  # Write to the file
finally:
    file.close()  # Close the file in any case, even if an exception occurs

# Another syntax using the with statement
with open("test.txt", "w") as file:  # Open file in write mode using with statement
    file.write("hello with another syntax")  # Write to the file


# Explanation:
    
# - The first approach uses a try finally block to ensure that
# the file is closed even if an exception occurs.

# - In the second approach, the with statement is used,
# which automatically closes the file when the block exits.
    
# - Both approaches achieve the same result of
# writing "hello" to the file "test.txt".
