# Problem: Choose a mode of transportation based on the
# distance (e.g., <3 km: Walk, 3-15 km: Bike, >15 km: Car).

distance = 5

if distance < 3:
    transport = "Walk"
elif distance <= 15:
    transport = "Bike"
else:
    transport = "Car"

print("Mode of transpotation based on the distance is {}".format(transport))