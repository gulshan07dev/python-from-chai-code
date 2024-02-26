## Behind the Scenes of Loops in Python

Before diving into the inner workings of Python loops, let's clarify some essential terms:

### 0. Iteration
Iteration refers to the process of looping through the objects or items in a collection.

### 1. Iteration Tool
Python provides various built-in tools like `for`, `comprehension`, `range()`, `enumerate()`, `map()`, `filter()`, etc., to efficiently work with iterations.

### 2. Iterable
An iterable is anything that we can iterate (loop) over. Examples include lists, strings, dictionaries, and tuples. Almost any object in Python can be made iterable.

### Iterator
An iterator is a value producer that yields successive values from its associated iterable object. The `next()` function is used to obtain the next value from an iterator.

### The Python `for` Loop

The `for` loop in Python is designed to iterate over elements of an iterable object. Here's how it works behind the scenes:

1. Obtain an iterator for the iterable using `iter()`.
2. Repeatedly call `next()` to obtain each item from the iterator.
3. Execute the loop body once for each item obtained from the iterator.
4. Terminate the loop when `next()` raises the `StopIteration` exception.

#### Example:
```python
myList = [1, 2, 3, 4]
myIter = iter(myList)

# Repeatedly call next() to obtain each item
print(next(myIter))  # Output: 1
print(next(myIter))  # Output: 2
print(next(myIter))  # Output: 3
print(next(myIter))  # Output: 4
```

The loop body is executed once for each item obtained from the iterator, with the loop variable set to the current item for each iteration.

--- 
## resource
 
video: https://www.youtube.com/watch?v=_VxQ5jzo37o&list=TLPQMjIwMjIwMjQJqQwNy29MrA&index=1&pp=gAQBiAQB
