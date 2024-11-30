# BEGIN: 9ycx9j4e449
def calculate_animals(legs):
    min_animals = legs // 4 + (legs % 4) // 2
    max_animals = legs // 2
    return min_animals, max_animals

a = int(input())
min_animals, max_animals = calculate_animals(a)
print(min_animals, max_animals)
# END: 9ycx9j4e449
