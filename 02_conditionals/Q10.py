# Problem: Recommend a type of pet food based on the pet's
# species and age. (e.g., Dog: <2 years - Puppy food,
# Cat: >5 years - Senior cat food).

species = input("Enter the species of your pet (dog or cat): ")
age = int(input("Enter the age of your pet: "))


if species.lower() == 'dog':
    if age < 2:
        print("Puppy food")
    else:
        print("Adult dog food")
elif species.lower() == 'cat':
    if age < 5:
        print("Adult cat food")
    else:
        print("Senior cat food")
else:
    print("Unknown species")