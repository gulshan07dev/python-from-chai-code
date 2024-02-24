# Problem: Print the multiplication table for a given number
# up to 10, but skip the fifth iteration.

table = 5

for i in range(1, 11):
    if i == 5:
        continue
    print("{} X {} = {}".format(table, i, table*i))