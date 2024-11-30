distance = int(input())
time_bike = distance / 3.0 + 27 + 23
time_walk = distance / 1.2
if time_bike < time_walk:
    print("Bike")
elif time_bike > time_walk:
    print("Walk")
else:
    print("All")
