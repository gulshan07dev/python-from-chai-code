# Problem: Write a generator function that yields even
# numbers up to a specified limit.

def even_generator(limit):
    for i in range(2, limit+1):
        yield i

for num in even_generator(10):
    print(num)