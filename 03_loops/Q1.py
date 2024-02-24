# Problem: Given a list of numbers, count how many are positive.
numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]

positiv_num_count = 0

for number in numbers:
    if number > 0:
        positiv_num_count += 1

print("Count of positive number is {}".format(positiv_num_count))