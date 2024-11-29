

def print_triangle(char):
    for i in range(3):
        spaces = ' ' * (2 - i)
        print(spaces, end='')
        print(char * (2 * i + 1), end='') 
        print(spaces, end='')
        print()
input_char = input()
print_triangle(input_char)
