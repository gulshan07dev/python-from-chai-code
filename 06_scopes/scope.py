# Scopes in Python

username = "chaiaurcode"  # Global variable

def func():
    # Uncomment the following line to create a local variable with the same name
    # username = "chai"  # Local variable
    print(username)  # Accessing the global variable 'username'

print(username)  # Output: chaiaurcode (Accessing the global variable 'username')
func()  # Output: chaiaurcode (Accessing the global variable 'username')

# Explanation:
# - The variable 'username' is defined outside the function 'func', making it a global variable.
# - When 'func' is called, it tries to print the value of 'username'. Since 'username' is not defined locally in 'func',
# Python looks for it in the enclosing scope, which is the global scope, and finds it as 'chaiaurcode'.
# - Therefore, both print statements inside and outside the function 'func' output 'chaiaurcode'.


# Closure in Python

def outer_func():
    name = "Gulshan"

    def inner_func():
        print(name)  # Accessing the variable 'name' from the outer function's scope

    return inner_func

my_func = outer_func()  # 'my_func' now holds the inner function 'inner_func'

my_func()  # Output: Gulshan

# Explanation:
# - In this example, 'outer_func' defines a variable 'name' and then defines another function 'inner_func' inside it.
# - 'inner_func' is a closure because it captures and remembers the value of the variable 'name' from its enclosing scope.
# - When 'my_func' is called, it executes 'inner_func', which still has access to the variable 'name' from the outer scope.
# - Therefore, 'inner_func' is able to print the value of 'message', which is "Hello".


# lets take one more example
 
def outer_func2(n):
    def inner_func2(num):
        print(num ** n)
    return inner_func2

square = outer_func2(2)  # 'square' now holds the inner function 'inner_func2' with 'n' set to 2

square(5)  # Output: 25 (5 raised to the power of 2)

# Explanation:
# - In this example, 'outer_func2' takes a parameter 'n' and defines an inner function 'inner_func2'.
# - 'inner_func2' calculates the square of its input argument 'num' raised to the power of 'n'.
# - When 'outer_func2(2)' is called, it returns 'inner_func2' with 'n' set to 2. This creates a closure.
# - The returned function is assigned to the variable 'square'.
# - When 'square(5)' is called, it executes 'inner_func2(5)', resulting in 5 ** 2, which is 25.

# Another Syntax:
outer_func2(2)(5)  # Output: 25

# Explanation:
# - This syntax directly calls the returned inner function of 'outer_func2(2)' with argument '5'.
# - It is equivalent to calling 'inner_func2(5)' after 'outer_func2(2)', resulting in the same output of 25.
