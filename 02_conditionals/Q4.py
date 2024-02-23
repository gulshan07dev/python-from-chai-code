# Problem: Determine if a fruit is ripe, overripe,
# or unripe based on its color. (e.g., Banana: Green - Unripe,
# Yellow - Ripe, Brown - Overripe)

fruit = "Banana"
color = "Yellow"

if fruit == "Banana":
    if color == "Green":
        print("Unripe")
    elif color == "Yellow":
        print("Ripe")
    elif color == "Brown":
        print("Overripe")
else:
    print("we have not information about this fruit")