# Understanding Mutability and Immutability in Python

In Python, everything is an object, including data types such as integers, strings, lists, dictionaries, etc. Objects in Python have properties, attributes, and methods associated with them.

## Object vs. Data Types (this is very imp for understanding next topic)
When we refer to "objects" in Python, we're essentially talking about data types. Every variable in Python refers to an object. Understanding the mutability and immutability of these data types is the foundation of python language.

## Immutable Objects

Immutable objects are those whose state (memory reference) cannot be modified after creation. If you want to change the value of an immutable object, you have to create a new object and assign it to the variable. Examples of immutable objects in Python include integers, booleans, floats, strings, and tuples.

### Example:

#### Strings:

Strings are immutable in Python. When you modify a string, you're actually creating a new string object and assigning it to the same variable name. Let's see an example:

```python
myName = "Gulshan"
print(myName)  # Output: Gulshan

myName = "Golu"
print(myName)  # Output: Golu
```

In the example above, when we assign `"Golu"` to the variable `myName`, we're actually creating a new string object in memory and assigning it to `myName`. The original string `"Gulshan"` remains unchanged.

### Note:

The confusion might arise because although it seems like we're modifying the value of `myName`, we're actually creating a new string object. This new object has a different memory reference from the original one.

---

## Mutable Objects

Mutable objects are those whose state (memory reference) can be modified after creation. Unlike immutable objects, you can directly modify the contents of mutable objects without creating a new object. Examples of mutable objects in Python include lists, dictionaries, and sets.

### Example:

#### Lists:

Lists are mutable in Python. You can modify the elements of a list directly. Let's see an example:

```python
myList = [1, 2, 3]
print(myList)  # Output: [1, 2, 3]

myList.append(4)
print(myList)  # Output: [1, 2, 3, 4]

myList[0] = 5
print(myList)  # Output: [5, 2, 3, 4]
```

In the example above, we modify the list `myList` directly by appending a new element (`4`) and changing the value of an existing element (`0th` index) to `5`. The changes are reflected in the same list object without creating a new one.

### Note:

Mutable objects allow direct modification of their contents. This means that changes to the object's state do not require creating a new object. Additionally, when you modify a mutable object, you're actually modifying the original object's memory reference.

### Changing Memory Reference:

Unlike immutable objects, modifying a mutable object does not involve changing the memory reference. Instead, you're directly modifying the object's contents. This means that the object remains at the same memory location, but its internal state may change.

---