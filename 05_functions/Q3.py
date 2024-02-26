# Problem: Write a function multiply that multiplies two numbers,
# but can also accept and multiply strings.

def multiply(p1, p2):
    if type(p1) == str and type(p2) == str:
        return "this multiplication is not possible"
    return p1 * p2

print(multiply(5, "h"))