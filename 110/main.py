# BEGIN: 9ycj4x9m4bfi
a = int(input())
b = int(input())
c = int(input())

square_area = a ** 2
rectangle_area = b * c

if square_area > rectangle_area:
    print("SQUARE")
elif rectangle_area > square_area:
    print("RECTANGLE")
else:
    print("SAME")
# END: 9ycj4x9m4bfi
