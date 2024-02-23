# Problem: Movie tickets are priced based on
# age: $12 for adults (18 and over), $8 for children.
# Everyone gets a $2 discount on Wednesday.

age = int(input("Enter your age: "))
isDayWednesday = input("Is day Wednesday? (True or False): ").lower() == 'true'

price = 12 if age >= 18 else 8

if isDayWednesday:
    price -= 2

print("Your Ticket Price is ${}".format(price))
