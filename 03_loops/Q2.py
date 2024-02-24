# Problem: Calculate the sum of even numbers up to a given number n.

n = 10

even_num_sum = 0
for i in range(1, n+1):
    if i % 2 == 0:
        even_num_sum += 1

print(even_num_sum)