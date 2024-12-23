def multiply_digits(n):
    result = 1
    for digit in str(n):
        result *= int(digit)
    return result


T = int(input())


for _ in range(T):
    n = int(input())
    print(multiply_digits(n))
