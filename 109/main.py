# BEGIN: 9ycx9j34x4wx
def sort_numbers(numbers):
    numbers.sort(reverse=True)
    return numbers

input_str = input()
numbers = [int(x) for x in input_str.split()]

sorted_numbers = sort_numbers(numbers)
for num in sorted_numbers:
    print(num, end=' ')
# END: 9ycx9j34x4wx
