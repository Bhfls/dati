def print_diamond(char):
    size = 5
    for i in range(size):
        spaces = " " * (size - i - 1)
        print(spaces, end="")
        print(char * (2 * i + 1), end="")  
        print(spaces, end="")
        print()

    for i in range(size - 2, -1, -1):
        spaces = " " * (size - i - 1)
        print(spaces, end="")
        print(char * (2 * i + 1), end="")  
        print(spaces, end="")
        print()

input_char = input()
print_diamond(input_char)
