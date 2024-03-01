# Problem: Create a decorator to print the function name
# and the values of its arguments every time the function is called.

def debug(func):
    def wrapper(*args, **kwargs):
        args_value = ', '.join(str(arg) for arg in args) if args else 0
        kwargs_value = ', '.join(str(arg) for arg in args) if kwargs else 0
        print(f"calling: {func.__name__} with args {args_value} and kwargs {kwargs_value}")
        return func(*args, **kwargs)
    return wrapper

@debug
def print_name(name, iteration):
    for i in range(iteration):
        print(name)

print_name("Gulshan", 2)