month, day = map(int, input().split())
if month < 2 or (month == 2 and day < 25):
    print("Pig")
else:
    print("Mouse")
